from src.GoogleCalendar import GoogleCalendar
from src.LeetCode import LeetCode

import json

def main():
    question = LeetCode().fetch_question()
    question = json.loads(question)

    event = GoogleCalendar()
    event.create_event(question)

if __name__ == "__main__":
    main()