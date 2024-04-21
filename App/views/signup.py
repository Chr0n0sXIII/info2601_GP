from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies

from App.controllers.user import get_all_users

from App.controllers import (
    create_user
)

signup_views = Blueprint('signup_views', __name__, template_folder='../templates')
@signup_views.route('/signup',methods=["GET"])
def signup_page():
    return render_template("signup.html")

@signup_views.route('/signup', methods=['POST'])
def signup_action():
    data = request.form
    create_user(data['username'],data['password'])
    signup_page()
    flash("Signup Sucessful")
    return render_template("signup.html", message =)