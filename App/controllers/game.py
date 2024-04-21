from App.models import (Score, User, Cipher, Game, Guess)
from App.database import db
from flask import g
from App.controllers import (iscow,isbull,update_moves, add_guess)

def create_game(user_id):
    cipher = Cipher.query.order_by(Cipher.id.desc()).first()

    score = Score(user_id)
    db.session.add(score)
    db.session.commit()
    game = Game(user_id,cipher.id,score.id)
    db.session.add(game)
    db.session.commit()
    return game

def get_game(game_id):
    return Game.query.filter_by(id =game_id).first()

def check_guess(game_id,digit1,digit2,digit3,digit4):
    game = get_game(game_id)
    update_moves(game.score_id)
    countBovine(game_id,digit1,digit2,digit3,digit4)

def get_all_user_games(user_id):
    return Game.query.filterby(user_id=user_id).all()

def get_all_games():
    return Game.query.all()

def get_game(score_id):
    return Game.query.filter_by(score_id = score_id). first()

def countBovine(game_id,digit1, digit2, digit3, digit4):
    game = get_game(game_id)
    bulls=0
    cows =0
    
    if isbull(game.cipher_id,digit1, 1) :
        bulls = bulls+1
    if isbull(game.cipher_id,digit2, 2) :
        bulls=bulls+1
    if isbull(game.cipher_id,digit3, 3) :
        bulls=bulls+1
    if isbull(game.cipher_id,digit4, 4) :
        bulls=bulls+1
    
    if iscow(game.cipher_id,digit1) and not isbull(game.cipher_id,digit1,1 ):
        cows+=1
    if iscow(game.cipher_id,digit2) and not isbull(game.cipher_id,digit2, 2):
        cows+=1
    if iscow(game.cipher_id,digit3) and not isbull(game.cipher_id,digit3, 3):
        cows+=1
    if iscow(game.cipher_id,digit4) and not isbull(game.cipher_id,digit4, 4):
        cows+=1
    
    if bulls == 4:
        game.win =1
        db.session.add(game)
        db.session.commit()
    add_guess(game.score_id,digit1,digit2,digit3,digit4, bulls, cows)

def delete_game(user_id):
    game = Game.query.filter_by(user_id = user_id).order_by(Game.id.desc()).first()
    score = Score.query.get(game.score_id)
    guesses = Guess.query.filter_by(score_id = score.id).all()
    db.session.delete(score)
    for guess in guesses:
        db.session.delete(guess)
    db.session.delete(game)
    db.session.commit()