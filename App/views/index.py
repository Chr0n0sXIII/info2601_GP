from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.models import db
from App.controllers import (create_user, create_cipher,)
from App.views import play
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    db.drop_all()
    db.create_all()
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=play.get_daily_cipher, trigger=CronTrigger(hour=0, minute=0))
    scheduler.start()
    cipher = create_cipher()
    print(cipher.get_json())
    create_user('bob', 'bobpass')
    return jsonify(message='db initialized!')

#@index_views.route('/create_cipher', methods =['GET'])
#def ccipher():
#    cipher = create_cipher()
#    json = cipher.get_json()
#    print(json)

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})

