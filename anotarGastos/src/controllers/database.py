import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET")
}