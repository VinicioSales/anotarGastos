#NOTE - Imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
import json
from src.static import paths
from src.funcs import html_convertor
from src.funcs import get_value
from src.funcs import integrating_google_spreadsheet
from src.funcs import searching_similar_values
from src.funcs import get_store
from src.funcs import get_expense_title_from_list
from src.static import variables as var
from datetime import datetime


date = datetime.now().strftime('%d/%m/%Y')
with open(f'{paths.files}/token_gmail.json', 'r') as token_file:
    token_info = json.load(token_file)

creds = Credentials.from_authorized_user_info(info=token_info)
service = build('gmail', 'v1', credentials=creds)
n_messages = 1


#NOTE - Filter
results = service.users().messages().list(userId='me', q=f'from:{var.sender_email} subject:{var.email_subject}', maxResults=n_messages).execute()
messages = results.get('messages', [])

#NOTE - Geting messeges
for message in messages:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    payload = msg['payload']
    headers = payload['headers']

    #NOTE - Getting the body
    if 'parts' in payload:
        parts = payload['parts']
        data = None
        for part in parts:
            if part['body'].get('data'):
                data = part['body']['data']
                break
        if data:
            data = base64.urlsafe_b64decode(data.encode('UTF-8')).decode('UTF-8')
    else:
        data = base64.urlsafe_b64decode(payload['body']['data'].encode('UTF-8')).decode('UTF-8')

#NOTE - Getting the value
converted_body = html_convertor(data=data)
value = get_value(text=converted_body)
print(f'value: {value}')
store = get_store(converted_body=converted_body)
print(f'store: {store}')

#NOTE - Google Sheet Interactions
with open(rf'{paths.files}\line_transacoes.txt', 'r') as file:
    line_transacoes = file.read()
sheet_resume = integrating_google_spreadsheet(sheet_id="Resumo")
sheet_transacoes = integrating_google_spreadsheet(sheet_id="Transações")

#NOTE - Getting expenses_title
expenses_title = get_expense_title_from_list(store=store)
if expenses_title == None:
    expenses_title = searching_similar_values(sheet_resume, value)
print(f"expenses_title: {expenses_title}")

#NOTE - Feeding sheet
sheet_transacoes.update_cell(line_transacoes, var.colum_data_transacoes, date)
sheet_transacoes.update_cell(line_transacoes, var.colum_valor_transacoes, value)
if expenses_title == None:
    sheet_transacoes.update_cell(line_transacoes, var.colum_categoria_transacoes, var.general)
else:
    sheet_transacoes.update_cell(line_transacoes, var.colum_categoria_transacoes, expenses_title)
line_transacoes = int(line_transacoes) + 1
with open(f'{paths.files}/line_transacoes.txt', 'w') as arquivo:
    arquivo.write(str(line_transacoes))
