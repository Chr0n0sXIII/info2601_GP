from App.database import db

class Score(db.Model):
    id = db.Column(db.Integer,primary_key=True ) 
    moves = db.Column(db.Integer,nullable = False)
    
    game = db.relationship('Game', backref='score')
    guesses = db.relationship('Guess',backref='score')

    def __init__(self, moves=-1):
        self.moves = moves
        self.bulls[0]= 0
        self.cows[0] = 0
             
    def get_json(self):
        return{
            'id':self.id,
            'bulls': self.bulls,
            'cows': self.cows,
            'moves': self.moves
         }
  
