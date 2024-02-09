import os
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from DailyQuestion import LeetCode
from dotenv import load_dotenv

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    credentials = flow.run_local_server(port=0)

    question = LeetCode().fetch_question()
    question = json.loads(question)

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

    calendar_id = os.getenv('GOOGLE_CAL_ID')
    
    service = build('calendar', 'v3', credentials=credentials)
    event = service.events().insert(calendarId=calendar_id, body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))

if __name__ == '__main__':
    main()