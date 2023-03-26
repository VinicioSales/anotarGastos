import os
from dotenv import load_dotenv

load_dotenv()

database_infos = {
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET"),
    "worksheet_id": "1A4ZXpo5lY4izxptb-a9Nq3l6V4odBKW0fsNngZj40tE"
}