from anotarGastos.src.funcs import grant_manual_access_gmail_api
from anotarGastos.src.funcs import create_token


creds = grant_manual_access_gmail_api()
create_token(creds)