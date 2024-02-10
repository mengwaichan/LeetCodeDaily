import requests
import json

class LeetCode:
    def __init__(self):
        self.url = "https://leetcode.com/graphql/"

    def fetch_question(self):
        headers = {
            'Content-Type': 'application/json',}

        data = {
            "query": """
                query questionOfToday {
                    activeDailyCodingChallengeQuestion {
                        date
                        userStatus
                        link
                        question {
                            acRate
                            difficulty
                            freqBar
                            frontendQuestionId: questionFrontendId
                            isFavor
                            paidOnly: isPaidOnly
                            status
                            title
                            titleSlug
                            hasVideoSolution
                            hasSolution
                            topicTags {
                                name
                                id
                                slug
                            }
                        }
                    }
                }
            """,
            "variables": {},
            "operationName": "questionOfToday"
        }

        response = requests.post(self.url, headers=headers, json = data)

        question = response.json()['data']['activeDailyCodingChallengeQuestion']['question']

        question_json = {
        "date": response.json()['data']['activeDailyCodingChallengeQuestion']['date'],
        "link": response.json()['data']['activeDailyCodingChallengeQuestion']['link'],
        "title": question['title'],
        "difficulty": question['difficulty'],
        "topicTags": [tag['name'] for tag in question['topicTags']],
        }

        json_result = json.dumps(question_json, indent=2)

        return json_result


if __name__ == '__main__':
    test = LeetCode()
    result = test.fetch_question()
    print(result)
