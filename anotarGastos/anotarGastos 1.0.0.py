#NOTE - Imports
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
import json
from src.static import paths
from src.funcs import html_convertor
from src.funcs import get_value
from src.funcs import integrating_google_spreadsheet
from src.static import variables



with open(f'{paths.files}/token_gmail.json', 'r') as token_file:
    token_info = json.load(token_file)

creds = Credentials.from_authorized_user_info(info=token_info)
service = build('gmail', 'v1', credentials=creds)
n_messages = 1


#NOTE - Filter
results = service.users().messages().list(userId='me', q='todomundo@nubank.com.br', maxResults=n_messages).execute()
messages = results.get('messages', [])


#NOTE - Geting messeges
for message in messages:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    payload = msg['payload']
    headers = payload['headers']

    #NOTE -  Getting data
    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']
        elif header['name'] == 'From':
            sender = header['value']
        elif header['name'] == 'Date':
            date = header['value']

    #NOTE -  Getting the body
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

    
print(f'Subject: {subject}')
print(f'From: {sender}')
print(f'Date: {date}')
#print(f'Body: {data}\n\n')

#NOTE - Getting the value
converted_body = html_convertor(data=data)
print(f"converted_body: {converted_body}")
value = get_value(text=converted_body)
print(value)

#NOTE - Google Sheet Interactions
with open(rf'{paths.files}\line_transations.txt', 'r') as file:
    line_transations = file.read()
sheet_resume = integrating_google_spreadsheet(sheet_id="Resumo")
sheet_transations = integrating_google_spreadsheet(sheet_id="Transações")
linha_planilha = 33
sheet_resume.update_cell(linha_planilha, variables.colum_real_resume, "=SE(ÉCÉL.VAZIA($B33); ""; SOMASE('Transações'!$E$"+line_transations+":$E;$B33;'Transações'!$C"+line_transations+":$C))")
