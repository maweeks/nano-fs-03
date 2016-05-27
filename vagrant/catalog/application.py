from flask import Flask, render_template, request, redirect, jsonify, flash
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
    developer = session.query(Developer).filter_by(id=game.d_id).one()
    othergames = session.query(Game).filter_by(d_id=game.d_id).filter(Game.id!=game_id).order_by(asc(Game.name)).all()
    return render_template('game.html', developer=developer, game=game, othergames=othergames)

# Show all games
@app.route('/games/')
def showGames():
    games = session.query(Game).order_by(asc(Game.name))
    return render_template('games.html', games=games)

# DB manipulation pages
# Create developer
@app.route('/developer/create', methods=['GET', 'POST'])
def createDeveloper():
    if request.method == 'POST':
        newDeveloper = Developer(name=request.form['name'], image=request.form['image'], description=request.form['description'], u_id=1)
        session.add(newDeveloper)
        session.commit()
        return redirect("/developers/")
    else:
        return render_template('createDeveloper.html')

# Edit developer
@app.route('/developer/<int:developer_id>/edit', methods=['GET', 'POST'])
def editDeveloper(developer_id):
    developer = session.query(Developer).filter_by(id=developer_id).one()
    if request.method == 'POST':
        developer.name = request.form['name']
        developer.image = request.form['image']
        developer.description = request.form['description']
        session.add(developer)
        session.commit()
        return redirect("/developer/"+str(developer.id)+"/")
    else:
        return render_template('editDeveloper.html', developer=developer)

# Delete developer and all their games
@app.route('/developer/<int:developer_id>/delete', methods=['GET', 'POST'])
def deleteDeveloper(developer_id):
    developer = session.query(Developer).filter_by(id=developer_id).one()
    if request.method == 'POST':
        session.delete(developer)
        games = session.query(Game).filter_by(d_id=developer_id).all()
        for game in games:
            session.delete(game)
        session.commit()
        return redirect("/developers/")
    else:
        return render_template('deleteDeveloper.html', developer=developer)

# Create game
@app.route('/developer/<int:developer_id>/game/create', methods=['GET', 'POST'])
def createGame(developer_id):
    if request.method == 'POST':
        newGame = Game(name=request.form['name'], image=request.form['image'], gameplay=request.form['gameplay'], description=request.form['description'], d_id=developer_id, u_id=1)
        session.add(newGame)
        session.commit()
        return redirect("/developer/"+str(developer_id))
    else:
        return render_template('createGame.html', developer_id=developer_id)

# Edit game
@app.route('/developer/<int:developer_id>/game/<int:game_id>/edit', methods=['GET', 'POST'])
def editGame(developer_id, game_id):
    game = session.query(Game).filter_by(id=game_id).one()
    if request.method == 'POST':
        game.name = request.form['name']
        game.image = request.form['image']
        game.gameplay = request.form['gameplay']
        game.description = request.form['description']
        session.add(game)
        session.commit()
        return redirect("/developer/"+str(game.d_id)+"/game/"+str(game.id)+"/")
    else:
        return render_template('editGame.html', developer_id=game.d_id, game=game)

# Delete game
@app.route('/developer/<int:developer_id>/game/<int:game_id>/delete', methods=['GET', 'POST'])
def deleteGame(developer_id, game_id):
    game = session.query(Game).filter_by(id=game_id).one()
    if request.method == 'POST':
        session.delete(game)
        session.commit()
        return redirect("/developer/"+str(game.d_id))
    else:
        return render_template('deleteGame.html', game=game)

# Custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)