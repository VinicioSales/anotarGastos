import os
import base64
import email
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from src.static import paths

# Caminho para o arquivo de credenciais JSON
credenciais_path = 'path/to/credenciais.json'

# Escopo da API do Gmail que será utilizada
escopo = ['https://www.googleapis.com/auth/gmail.readonly']

# Cria as credenciais a partir do arquivo de credenciais
credenciais = Credentials.from_authorized_user_file(f'{paths.files}/credencials.json', escopo)

# Cria a conexão com a API do Gmail
servico_gmail = build('gmail', 'v1', credentials=credenciais)

# Lista os e-mails da caixa de entrada
resultados = servico_gmail.users().messages().list(userId='me', maxResults=10).execute()

# Percorre a lista de mensagens e obtém o corpo da mensagem
for mensagem in resultados['messages']:
    # Obtém o ID da mensagem
    id_mensagem = mensagem['id']
    # Obtém os dados da mensagem
    dados_mensagem = servico_gmail.users().messages().get(userId='me', id=id_mensagem).execute()
    # Obtém o corpo da mensagem
    partes = dados_mensagem['payload']['parts']
    for parte in partes:
        if parte['mimeType'] == 'text/plain':
            corpo_mensagem = parte['body']['data']
            # Decodifica o corpo da mensagem
            corpo_decodificado = base64.urlsafe_b64decode(corpo_mensagem).decode()
            print(corpo_decodificado)
