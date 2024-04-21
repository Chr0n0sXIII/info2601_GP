from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for,g
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from App.models import Game, Score, User, Cipher
from App.controllers import (
    get_user,
    get_all_users,
    get_all_users_json,
    get_all_scores,
    get_all_games,
    get_all_scores_json,
    get_score,
    get_game,
    jwt_required
)

leaderboard_views = Blueprint('leaderboard_views', __name__, template_folder='../templates')

@leaderboard_views.route('/leaderboard',methods=["GET"])
@jwt_required()
def leaderboard_page():
    cipher = Cipher.query.order_by(Cipher.id.desc()).first()
    games = Game.query.filter_by(cipher_id = cipher.id).all()
    score_id = [game.score_id for game in games]

    scores = Score.query.filter(Score.id.in_(score_id)).order_by(Score.moves.asc()).all()
    leaderboardinfo = {}
    allscores =[]
    for score in scores:
        game = get_game(score.id)
        if(game.win == 1):
            user = get_user(game.user_id)
            leaderboardinfo = {
                "username":user.username,
                "moves":score.moves
            }
            allscores.append(leaderboardinfo)
    return render_template("leaderboard.html",leaderboardinfo = allscores)

