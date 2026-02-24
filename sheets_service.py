import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from datetime import datetime

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1zG_0dNdwZdJ-pPvtptq5TSjYT9yNHFTMThqS8kxqcWk"
RANGE = "Sheet1!A:E"

creds = Credentials.from_service_account_file(
    "credentials.json",
    scopes=SCOPES
)

service = build("sheets", "v4", credentials=creds)
sheet = service.spreadsheets()

def read_users():
    result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE
    ).execute()
    return result.get("values", [])

def add_user(email, password_hash, role, insight):
    timestamp = str(datetime.now())

    sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE,
        valueInputOption="RAW",
        body={
            "values": [[email, password_hash, role, timestamp, insight]]
        }
    ).execute()