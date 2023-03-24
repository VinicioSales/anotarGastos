from google_auth_oauthlib.flow import InstalledAppFlow
from controllers.database import database_infos
import json

def liberar_acesso_manual():
    #NOTE - liberar_acesso_manual
    """
    This function requests user authorization to access Gmail API.
    
    It reads the client ID and client secret from the 'database_infos' dictionary and creates 
    a flow object with the appropriate parameters. Then, it runs the flow object to get the 
    user authorization and returns the credentials object for further usage.
    
    Returns:
        - creds
    """
    client_id = database_infos['client_id']
    client_secret = database_infos['client_secret']
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    flow = InstalledAppFlow.from_client_config(
        {
            "installed": {
                "client_id": client_id,
                "project_id": "notificacoes-381501",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_secret": client_secret,
                "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
            }
        },
        scopes=SCOPES
    )

    creds = flow.run_local_server(port=0)
    creds = flow.credentials

    return creds


def criar_token(creds):
    #NOTE - criar_token
    """
    This function creates a JSON token file containing the user's credentials information.
    
    It takes a credentials object as input and extracts the relevant information such as the 
    access token, refresh token, token URI, client ID, client secret, and scopes. It then writes 
    this information to a JSON file named 'token.json' in the current working directory.
    
    Args:
        creds: A credentials object to access Gmail API.
    """
    
    with open('token.json', 'w') as token_file:
        json.dump({
            'token': creds.token,
            'refresh_token': creds.refresh_token,
            'token_uri': creds.token_uri,
            'client_id': creds.client_id,
            'client_secret': creds.client_secret,
            'scopes': creds.scopes
        }, token_file)