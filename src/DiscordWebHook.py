import requests

class Discord():
    def __init__(self, url) -> None:
        self.webhook_url = url
    
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
            print("Message delivered to Discord successfully, code {}.".format(response.status_code))