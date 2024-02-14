from src.GoogleCalendar import GoogleCalendar
from src.LeetCode import LeetCode
from src.DiscordWebHook import Discord
import json

def main():
    question = LeetCode().fetch_question()
    question = json.loads(question)

    event = GoogleCalendar()
    event.load_credentials()
    event.create_event(question)

    discord = Discord()
    discord.send_message(question)

if __name__ == "__main__":
    main()

