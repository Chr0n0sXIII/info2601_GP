
from App.database import db

class Game(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    cipher_id = db.Column(db.Integer, db.ForeignKey('cipher.id'), nullable=False)
    score_id = db.Column(db.Integer, db.ForeignKey('score.id'), nullable = False)
    win = db.Column(db.Integer, nullable = False)

    def __init__(self,user_id,cipher_id, score_id):
        self.cipher_id=cipher_id
        self.score_id=score_id
        self.user_id = user_id
        win = 0

    def get_json(self):
        return{
            'id':self.id,
            'user_id': self.user_id,
            'cipher_id':self.cipher_id,
            'score_id': self.score_id

        }

        