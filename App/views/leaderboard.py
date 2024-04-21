from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for,g
from flask_jwt_extended import jwt_required, current_user as jwt_current_user

from App.models import Game, Score, User
from App.controllers import (
    get_user,
    get_all_users,
    get_all_users_json,
    get_all_scores,
    get_all_games,
    get_all_scores_json,
    get_score,
    jwt_required
)

leaderboard_views = Blueprint('leaderboard_views', __name__, template_folder='../templates')

@leaderboard_views.route('/leaderboard',methods=["GET"])
@jwt_required()
def leaderboard_page():
    users = get_all_users()
    scores = get_all_scores()
    userscores = []
    leaderboardinfo = {}
    lowestscore = 99
    userscore = 99
    for user in users:
        print("userscore: ", get_score(user.id))
        userscore = get_score(user.id)
        if userscore == None:
            userscore = 99
        leaderboardinfo = {
            "username":user.username,
            "userscore":userscore
        }
        if userscore < lowestscore:
            lowestscore = userscore
        userscores.append(leaderboardinfo)
        leaderboardinfo = {}
    userscores.sort(key=lambda x: x['userscore'])

    return render_template("leaderboard.html", allusers=users, allscores=scores, boardinfo=userscores)


