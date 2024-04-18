from sqlalchemy import ForeignKey
from App.database import db

class Guess(db.Model):
  id= db.Column(db.Integer, primary_key=True)
  digit1 =db.Column(db.Integer, nullable=False)
  digit2 =db.Column(db.Integer, nullable=False)
  digit3 =db.Column(db.Integer, nullable=False)
  digit4 =db.Column(db.Integer, nullable=False)
  score_id=db.Column(db.Integer, db.ForeignKey('score.id'), nullable=False)
  
def __init__(self, digit1, digit2, digit3, digit4, score_id):
  self.digit1 = digit1
  self.digit2 = digit2
  self.digit3 = digit3
  self.digit4 = digit4
  self.score_id = score_id