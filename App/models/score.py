from App.database import db

class Score(db.Model):
    id = db.Column(db.Integer,primary_key=True ) 
    moves = db.Column(db.Integer,nullable = False)
    game = db.relationship('Game', backref='score')
    guesses = db.relationship('Guess',backref='score')

    def __init__(self, moves=-1):
        self.moves = moves
        
             
    def get_json(self):
        return{
            'id':self.id,
            'moves': self.moves
         }
  
