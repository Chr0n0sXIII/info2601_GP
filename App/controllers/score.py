from App.models import Score
from App.database import db

def create_score(user_id, cipher_id):
    newscore = Score(user_id=user_id, cipher_id=cipher_id)
    db.session.add(newscore)
    db.session.commit()
    return newscore

def get_scores_by_user_id(user_id):
    return Score.query.filter_by(user_id=user_id).all()

def get_score(id):
    return Score.query.filter_by(id=id).first()

def get_scores_by_cipher_id(cipher_id):
    return Score.quert.filter_by(cipher_id = cipher_id).all()

def get_all_scores():
    return Score.query.all()

def get_all_scores_json():
    scores = Score.query.all()
    if not scores:
        return []
    scores = [score.get_json() for score in scores]
    return scores

def update_scores(id, moves):
    score = get_score(id)
    if score:
        score.moves = moves
        db.session.add(score)
        return db.session.commit()
    return None