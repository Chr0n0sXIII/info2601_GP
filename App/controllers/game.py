from App.models import (Score, User, Cipher, Game)
from App.database import db
from flask import g
from App.controllers import (iscow,isbull,update_moves,update_bovine)

def create_game(user_id):
    cipher = g.daily_cipher
    score = Score(user_id)
    game = Game(user_id,cipher.id,score.id)
    db.session.add(score)
    db.session.add(game)
    db.session.commit()
    return game
def get_game(game_id):
    return Game.query.filter_by(id =game_id).first()

def guess(game_id,digit1,digit2,digit3,digit4):
    game = get_game(game_id)
    update_moves(game.score_id)
    guess= {
        'digit1':digit1,
        'digit2':digit2,
        'digit3':digit3,
        'digit4': digit4}
    add_guess(game.score_id,guess)
    countBovine(game_id,digit1,digit2,digit3,digit4)

    
def countBovine(game_id,digit1, digit2, digit3, digit4):
    game = get_game(game_id)
    bulls=0
    cows =0
    if isbull(game.cipher_id,digit1, 1) :
        bulls+=1
        if isbull(game.cipher_id,digit2, 2) :
            bulls+=1
            if isbull(game.cipher_id,digit3, 3) :
                bulls+=1
                if isbull(game.cipher_id,digit4, 4) :
                    bulls+=1
    
    if iscow(game.cipher_id,digit1):
        cows+=1
        if iscow(game.cipher_id,digit2):
            cows+=1
            if iscow(game.cipher_id,digit3):
                cows+=1
                if iscow(game.cipher_id,digit4):
                    cows+=1
    
    update_bovine(game.score_id,bulls,cows)