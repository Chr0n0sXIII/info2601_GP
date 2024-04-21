from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies

from App.models import User

from App.controllers import (
    create_user,
    get_all_users
)

signup_views = Blueprint('signup_views', __name__, template_folder='../templates')
@signup_views.route('/signup',methods=["GET"])
def signup_page():
    return render_template("signup.html")

@signup_views.route('/signup', methods=['POST'])
def signup_action():
    data = request.form
    user = User.query.filter_by(username=data['username']).first()
    if not(user):
        create_user(data['username'],data['password'])     
        flash("Signup Sucessful")
    else:    
        flash('Username already in use')
    return render_template("signup.html")
