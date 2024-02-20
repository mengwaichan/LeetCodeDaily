import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import pickle

class GoogleCalendar:
    def __init__(self, calendar_id):
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.calendar_id = calendar_id
        
        self.credentials = None
    
    def load_credentials(self):
        if os.path.exists('./token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.credentials = pickle.load(token)
        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('./credentials.json', self.SCOPES)
                self.credentials = flow.run_local_server(port=0)
            with open('./token.pickle', 'wb') as token:
                pickle.dump(self.credentials, token)

    def create_event(self, question):
        event = {
            'summary': question['title'],
            'location': question["link"],
            'description': f'Difficulty: {question["difficulty"]}',
            'start': {
                'date':question["date"],
                'timeZone': 'America/New_York', 
                },
            'end': {
                'date':question["date"],
                'timeZone': 'America/New_York',
                },
        }

        try:
            service = build('calendar', 'v3', credentials=self.credentials)
            event = service.events().insert(calendarId=self.calendar_id, body=event).execute()
            print('Event created: %s' % (event.get('htmlLink')))
        except HttpError as e:
            print(f'An HTTP error occurred: {e}')
        except Exception as e:
            print(f'An error occurred: {e}')
