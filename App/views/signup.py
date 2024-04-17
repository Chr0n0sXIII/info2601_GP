from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies

from App.controllers.user import get_all_users

from App.controllers import (
    cipher,score,user
)

signup_views = Blueprint('signup_views', __name__, template_folder='../templates')
@signup_views.route('/signup',methods=["GET"])
@jwt_required()
def signup_page():
    return render_template("play.html")