from src.google_calendar import GoogleCalendar
from src.leetcode import LeetCode
from src.discord_webhook import Discord
from src.firebase import Firebase

from dotenv import load_dotenv
import os
import json
from flask import Flask, jsonify

load_dotenv()
app = Flask(__name__)

@app.route('/')
def create():
    response = {"status": "success"}

    try:
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
    except Exception as e:
        response["status"] = "error"
        response["message"] = str(e)

    return jsonify(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
