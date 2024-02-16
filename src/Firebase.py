import firebase_admin
from firebase_admin import firestore, credentials
from datetime import datetime

class Firebase:
    def __init__(self):
        self.cred = None
    
    def init_cred(self):
        self.cred = credentials.Certificate('./firebase_auth.json')
        firebase_admin.initialize_app(self.cred)

    def insert_question(self, question):
        date = datetime.strptime(question['date'], "%Y-%m-%d") 
        month = date.strftime("%B")
        year = date.strftime("%Y")

        db_ref = firestore.client().collection(year).document(month)
        
        question_ref = db_ref.collection(question['date'])
        question_ref.add(question)

        print("New question inserted to database")
    
    