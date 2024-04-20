from App.models import (Score, User, Cipher, Game, Guess)
from App.database import db
from flask import g
from App.controllers import (iscow,isbull,update_moves, add_guess)

def create_game(user_id):
    cipher = Cipher.query.order_by(Cipher.id.desc()).first()
    if not cipher:
        print('no cipher')
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


    
def countBovine(game_id,digit1, digit2, digit3, digit4):
    game = get_game(game_id)
    bulls=0
    cows =0
    
    if isbull(game.cipher_id,digit1, 1) :
        bulls = bulls+1
        print('bull+1')
    if isbull(game.cipher_id,digit2, 2) :
        bulls=bulls+1
        print('bull+1')
    if isbull(game.cipher_id,digit3, 3) :
        bulls=bulls+1
        print('bull+1')
    if isbull(game.cipher_id,digit4, 4) :
        bulls=bulls+1
        print('bull+1')
    
    if iscow(game.cipher_id,digit1):
        cows+=1
        print('cow+1')
    if iscow(game.cipher_id,digit2):
        cows+=1
        print('cow+1')
    if iscow(game.cipher_id,digit3):
        cows+=1
        print('cow+1')
    if iscow(game.cipher_id,digit4):
        cows+=1
        print('cow+1')
    
    add_guess(game.score_id,digit1,digit2,digit3,digit4, bulls, cows)
