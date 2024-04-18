from App.models import Score
from App.database import db

def create_score():
    newscore = Score()
    db.session.add(newscore)
    db.session.commit()
    return newscore

def get_score(id):
    return Score.query.filter_by(id=id).first()

def get_all_scores():
    return Score.query.all()

def get_all_scores_json():
    scores = Score.query.all()
    if not scores:
        return []
    scores = [score.get_json() for score in scores]
    return scores

def update_moves(id):
    score = get_score(id)
    if score:
        score.moves +=1
        db.session.add(score)
        db.session.commit()
    return None

def update_bovine(id,bulls, cows):
    score = get_score(id)
    score.bulls[score.moves]=bulls
    score.cows[score.moves]=cows

    db.session.add(score)
    db.session.commit()

def add_guess(id,digit1,digit2,digit3,digit4):
    score = get_score(id)
    guess = Guess(digit1,digit2,digit3,digit4,id)
    db.session.add(guess)
    db.session.commit()