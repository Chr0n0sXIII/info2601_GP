import random
from sqlalchemy import DateTime
from App.database import db

class Cipher(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime,nullable=False)
    digit1 = db.Column(db.Integer,nullable=False)
    digit2 = db.Column(db.Integer,nullable = False)
    digit3 = db.Column(db.Integer, nullable = False)
    digit4 = db.Column(db.Integer,nullable = False)
    bulls = db.Column(db.Integer,nullable = False)
    cows = db.Column(db.Integer, nullable = False)
    scores = db.relationship('Score',backref='cipher')

    def __init__(self):
        self.date = DateTime.now
        self.generate_numbers()
        bulls = 0
        cows = 0

    def generate_unique_digits():
        digits = random.sample(range(10), 4)  # Generate a list of 4 unique digits
        return digits

    def generate_numbers(self):
        unique_digits = self.generate_unique_digits()
        self.digit1, self.digit2, self.digit3, self.digit4 = unique_digits
    
    def get_json(self):
        return{
            'id': self.id,
            'date':self.date,
            'digit 1' : self.digit1,
            'digit 2' : self.digit2,
            'digit 3' : self.digit3,
            'digit 4' : self.digit4,
            'bulls' : self.bulls,
            'cows' : self.cows
        }
