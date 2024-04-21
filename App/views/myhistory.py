from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for,g
from flask_jwt_extended import jwt_required, get_jwt_identity

from App.models import Game, Score, User, Cipher
from App.controllers import (
    get_user,
    get_all_users,
    get_all_users_json,
    get_all_scores,
    get_all_user_games,
    get_all_scores_json,
    get_score,
    get_game,
    jwt_required
)

myhistory_views = Blueprint('myhistory_views',__name__,template_folder='../template')

@myhistory_views.route('/myhistory',methods=['GET'])
def myhistory_page():
   return get_data()

@jwt_required()
def get_data():
    user_id = get_jwt_identity()
    games = get_all_user_games(user_id)
    scores ={}
    allscores=[]
    for game in games:
        if(game.win ==1):
            cipher = Cipher.query.filter_by(id=game.cipher_id).first()
            score = get_score(game.score_id)
            scores = {
                    "cipher":cipher,
                    "score":score.moves
                }
            allscores.append(scores)
    return render_template('myhistory.html',history=allscores)