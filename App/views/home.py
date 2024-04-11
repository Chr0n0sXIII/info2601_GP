from flask import Blueprint, render_template, jsonify, request, flash, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies

from App.controllers.user import get_all_users

from App.controllers import (
    cipher,score,user
)

home_views = Blueprint('home_views',__name__,template_folder="..//template")

@home_views.route('/home', methods=['GET'])
def get_home_page():
    return render_template('home.html')