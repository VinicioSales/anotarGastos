from google_auth_oauthlib.flow import InstalledAppFlow
from src.controllers.database import database_infos
import json
from bs4 import BeautifulSoup
import html2text
from oauth2client.service_account import ServiceAccountCredentials
import re
import gspread
from src.static import paths
from src.static import variables as var



def grant_manual_access_gmail_api():
    #NOTE - grant_manual_access_gmail_api
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


def create_token(creds):
    #NOTE - create_token
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

def html_convertor(data):
    #NOTE - html_convertor
    """
    This function converts HTML data to plain text format.

    It takes HTML data as input and uses the BeautifulSoup library to parse the data into an 
    HTML tree. Then, it uses the html2text library to convert the tree into plain text format.
    
    Args:
        str: data: HTML data to be converted to plain text format.
        
    Returns:
        str: text
    """
    soup = BeautifulSoup(data, 'html.parser')
    text = html2text.html2text(soup.prettify())

    return text

def integrating_google_spreadsheet(sheet_id):
    #NOTE - integrando_google_planilha
    """
    Integra a planilha do google
    
    params:
        - string: sheet_id
    
    returns:
        - sheet: planilha"""
    
    worksheet_id = database_infos['worksheet_id']
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(f'{paths.files}/credentials_planilha.json', scope)
    gc = gspread.authorize(credentials)
    wks = gc.open_by_key(worksheet_id)
    sheet = wks.worksheet(sheet_id)
    print(f"sheet: {sheet}")

    return sheet

def get_value(text):
    #NOTE - get_value
    """
    Extracts a monetary value from a given text using regular expression.

    args:
        - str: text

    returns:
        - str: value
    """
    regular_expression = r"\d{1,3}(?:\.\d{3})*(?:,\d{2})?"
    result = re.search(regular_expression, text)
    value = result.group()

    return value

def searching_similar_values(sheet_resume, value):
    #NOTE - searching_similar_values
    """Search for a row in the sheet_resume containing a value similar to the given value parameter.

    params:
        - str: value

    returns:
        - str: expenses_title
    """
    search_row = sheet_resume.find(f'R$ {value}', in_column=var.colum_planejado) 
    if str(search_row) != 'None':
        line_num = search_row.row
        line_values = sheet_resume.row_values(line_num)
        expenses_title = line_values[1]

        return expenses_title
    else:
        return None

