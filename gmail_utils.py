import os

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

def gmail_auth():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )

            creds = flow.run_local_server(
                port=8088,
                open_browser=False
            )

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build(
        "gmail",
        "v1",
        credentials=creds
    )


def get_latest_emails(limit=5):
    service = gmail_auth()

    results = service.users().messages().list(
        userId="me",
        maxResults=limit
    ).execute()

    messages = results.get("messages", [])

    output = []

    for msg in messages:
        data = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        output.append(
            data.get("snippet", "")
        )

    return output


def search_emails(query, limit=5):
    service = gmail_auth()

    results = service.users().messages().list(
        userId="me",
        q=query,
        maxResults=limit
    ).execute()

    messages = results.get("messages", [])

    output = []

    for msg in messages:
        data = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        output.append(
            data.get("snippet", "")
        )

    return output
