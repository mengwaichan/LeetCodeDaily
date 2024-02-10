import os
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dotenv import load_dotenv

class GoogleCalendar:
    def __init__(self):
        load_dotenv()
        self.SCOPES = ['https://www.googleapis.com/auth/calendar']
        self.calendar_id = os.getenv('GOOGLE_CAL_ID')
        flow = InstalledAppFlow.from_client_secrets_file('./credentials.json', self.SCOPES)
        self.credentials = flow.run_local_server(port=0)

    def create_event(self, question):
        event = {
            'summary': question['title'],
            'location': 'https://leetcode.com'+ question["link"],
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

        service = build('calendar', 'v3', credentials=self.credentials)
        event = service.events().insert(calendarId=self.calendar_id, body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))
