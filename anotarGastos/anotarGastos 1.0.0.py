from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import base64
import json
from src.static import paths


with open(f'{paths.files}\token.json', 'r') as token_file:
    token_info = json.load(token_file)

creds = Credentials.from_authorized_user_info(info=token_info)

# Criar um objeto da API do Gmail
service = build('gmail', 'v1', credentials=creds)

n_messages = 5


# Recuperar a lista de IDs das mensagens
results = service.users().messages().list(userId='me', maxResults=n_messages).execute()
messages = results.get('messages', [])


# Loop pelas mensagens e recuperar seus dados
for message in messages:
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    payload = msg['payload']
    headers = payload['headers']

    # Loop pelas informações dos cabeçalhos para obter o assunto, remetente e data
    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']
        elif header['name'] == 'From':
            sender = header['value']
        elif header['name'] == 'Date':
            date = header['value']

    # Recuperar o corpo da mensagem
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

    # Imprimir os dados recuperados
    print(f'Subject: {subject}')
    print(f'From: {sender}')
    print(f'Date: {date}')
    print(f'Body: {data}\n\n')