from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc, desc
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
# JSON for all developers
@app.route('/JSON')
@app.route('/developers/JSON')
def developersJSON():
    developers = session.query(Developer).all()
    return jsonify(developers=[r.serialize for r in developers])

# JSON for all a single developer's games
@app.route('/developer/<int:developer_id>/JSON')
@app.route('/developer/<int:developer_id>/games/JSON')
def developerGamesJSON(developer_id):
    developer = session.query(Developer).filter_by(id=developer_id).one()
    games = session.query(Game).filter_by(d_id=developer_id).all()
    return jsonify(games=[i.serialize for i in games])

# JSON for single game
@app.route('/developer/<int:developer_id>/game/<int:game_id>/JSON')
def gameJSON(developer_id, game_id):
    game = session.query(Game).filter_by(id=game_id).one()
    return jsonify(game=game.serialize)

# JSON for all games
@app.route('/games/JSON')
def gamesJSON():
    games = session.query(Game).all()
    return jsonify(games=[i.serialize for i in games])


# HTML pages
# Show index (latest games and all developers)
@app.route('/')
@app.route('/index/')
def showIndex():
    developers = session.query(Developer).order_by(asc(Developer.name))
    latest = session.query(Game).order_by(desc(Game.id)).limit(6)
    return render_template('index.html', developers=developers, latest=latest)

# Show all developers
@app.route('/developers/')
def showDevelopers():
    developers = session.query(Developer).order_by(asc(Developer.name))
    return render_template('developers.html', developers=developers)

# Show single developer page
@app.route('/developer/<int:developer_id>/')
@app.route('/developer/<int:developer_id>/games')
def developer(developer_id):
    developer = session.query(Developer).filter_by(id=developer_id).one()
    games = session.query(Game).filter_by(d_id=developer_id).order_by(asc(Game.name)).all()
    return render_template('developer.html', developer=developer, games=games)

# Show a single game
@app.route('/developer/<int:developer_id>/game/<int:game_id>/')
def game(developer_id, game_id):
    game = session.query(Game).filter_by(id=game_id).one()
    developer = session.query(Developer).filter_by(id=developer_id).one()
    othergames = session.query(Game).filter_by(d_id=developer_id).filter(Game.id!=game_id).order_by(asc(Game.name)).all()
    return render_template('game.html', developer=developer, game=game, othergames=othergames)

# Show all games
@app.route('/games/')
def showGames():
    games = session.query(Game).order_by(asc(Game.name))
    return render_template('games.html', games=games)

# DB manipulation pages
# Create developer
@app.route('/developer/create')
@app.route('/developers/create')
def createDeveloper():
    return "Create developer."

# Edit developer
@app.route('/developer/<int:developer_id>/edit')
def editDeveloper(developer_id):
    return "Edit developer: " + str(developer_id)

# Delete developer
@app.route('/developer/<int:developer_id>/delete')
def deleteDeveloper(developer_id):
    return "Delete developer: " + str(developer_id)

# Create game
@app.route('/developer/<int:developer_id>/game/create')
def createGame(developer_id):
    return "Create game for: " + str(developer_id)

# Edit game
@app.route('/developer/<int:developer_id>/game/<int:game_id>/edit')
def editGame(developer_id, game_id):
    return "Edit game: " + str(game_id)

# Delete game
@app.route('/developer/<int:developer_id>/game/<int:game_id>/delete')
def deleteGame(developer_id, game_id):
    return "Delete game: " + str(game_id)

# Custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)