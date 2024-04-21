from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, url_for
from App.models import db
from App.controllers import (create_user, create_cipher,)
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from App.views import play

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return check_auth_token()

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=play.get_daily_cipher, trigger=CronTrigger(hour=0, minute=0))
    scheduler.start()
    create_cipher()
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

def check_auth_token():   
    # Check if an auth token is present in the request headers
    if 'Authorization' in request.headers:
        return redirect(url_for('home_page'))
    return render_template("index.html")

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

