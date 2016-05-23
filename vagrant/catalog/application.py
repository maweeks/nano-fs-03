from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Developer, Game
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

engine = create_engine('sqlite:///gamecatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# JSON pages
@app.route('/JSON')
@app.route('/developers/JSON')
def developersJSON():
    developers = session.query(Developer).all()
    return jsonify(developers=[r.serialize for r in developers])

@app.route('/developer/<int:developer_id>/JSON')
@app.route('/developer/<int:developer_id>/games/JSON')
def developerGamesJSON(developer_id):
    developer = session.query(Developer).filter_by(id=developer_id).one()
    games = session.query(Game).filter_by(d_id=developer_id).all()
    return jsonify(Games=[i.serialize for i in games])

@app.route('/developer/<int:developer_id>/game/<int:game_id>/JSON')
def gameJSON(developer_id, game_id):
    game = session.query(Game).filter_by(id=game_id).one()
    return jsonify(game=game.serialize)




# HTML pages
# Show all developers
@app.route('/')
@app.route('/index/')
def showIndex():
    return render_template('index.html', developers=developers)




@app.route('/developers/')
def showDevelopers():
    developers = session.query(Developer).order_by(asc(Developer.name))
    # if 'username' not in login_session:
        # return render_template('publicdevelopers.html', developers=developers)
    # else:
        # return render_template('developers.html', developers=developers)
    return "Developer."

# Login pages


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)