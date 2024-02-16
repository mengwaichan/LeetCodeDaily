from src.GoogleCalendar import GoogleCalendar
from src.LeetCode import LeetCode
from src.DiscordWebHook import Discord
from src.Firebase import Firebase

from dotenv import load_dotenv
import os
import json
from flask import Flask

load_dotenv()
app = Flask(__name__)


@app.route('/')
def create():
    question = LeetCode().fetch_question()
    question = json.loads(question)

    event = GoogleCalendar(os.getenv("GOOGLE_CAL_ID"))
    event.load_credentials()
    event.create_event(question)

    discord = Discord(os.getenv('DISCORD_URL'))
    discord.send_message(question)
    
    db = Firebase()
    db.init_cred()
    db.insert_question(question)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)


