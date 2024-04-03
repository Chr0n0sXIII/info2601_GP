from App.database import db

class Score(db.Model):
    id = db.Column(db.Integer,primary_key=True ) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    cipher_id = db.Column(db.Integer, db.ForeignKey('cipher.id'),nullable = False)
    moves = db.Column(db.Integer,nullable = False)
    

    def __init__(self, user_id, cipher_id, moves):
        self.user_id = user_id
        self.cipher_id = cipher_id
        self.moves = moves
             
    def get_json(self):
        return{
            'id':self.id,
            'user id': self.user_id,
            'cipher id': self.cipher_id,
            'moves': self.moves
         }
  
