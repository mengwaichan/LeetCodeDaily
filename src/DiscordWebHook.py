import requests
import json
import os
from dotenv import load_dotenv

class Discord():
    def __init__(self) -> None:
        load_dotenv()
        self.webhook_url = os.getenv("DISCORD_URL")
    
    def send_message(self, question):
        
        data = {
            "content" : "@everyone",
            "username": "Leetcode"
        }

        data["embeds"] = [
            {
                "description" : f'Difficulty: {question["difficulty"]}',
                "url" : 'https://leetcode.com'+ question["link"],
                "title": question['title']
            }
        ]

        response = requests.post(self.webhook_url, json = data)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(response.status_code))