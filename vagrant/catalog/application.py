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

CLIENT_ID = json.loads(open('client_secrets.json', 'r').read())['web']['client_id']

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
    return render_template('index.html', developers=developers, latest=latest, visibility=checkUserID(login_session))

# Show all developers
@app.route('/developers/')
def showDevelopers():
    developers = session.query(Developer).order_by(asc(Developer.name))
    return render_template('developers.html', developers=developers, visibility=checkUserID(login_session))

# Show single developer page
@app.route('/developer/<int:developer_id>/')
@app.route('/developer/<int:developer_id>/games')
def developer(developer_id):
    developer = session.query(Developer).filter_by(id=developer_id).one()
    games = session.query(Game).filter_by(d_id=developer_id).order_by(asc(Game.name)).all()
    return render_template('developer.html', developer=developer, games=games, visibility=checkUserID(login_session))

# Show a single game
@app.route('/developer/<int:developer_id>/game/<int:game_id>/')
def game(developer_id, game_id):
    game = session.query(Game).filter_by(id=game_id).one()
    developer = session.query(Developer).filter_by(id=game.d_id).one()
    othergames = session.query(Game).filter_by(d_id=game.d_id).filter(Game.id!=game_id).order_by(asc(Game.name)).all()
    return render_template('game.html', developer=developer, game=game, othergames=othergames, visibility=checkUserID(login_session))

# Show all games
@app.route('/games/')
def showGames():
    games = session.query(Game).order_by(asc(Game.name))
    return render_template('games.html', games=games, visibility=checkUserID(login_session))

# DB manipulation pages
# Create developer
@app.route('/developer/create', methods=['GET', 'POST'])
def createDeveloper():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newDeveloper = Developer(name=request.form['name'], image=request.form['image'], description=request.form['description'], u_id=login_session['user_id'])
        session.add(newDeveloper)
        session.commit()
        flash('Developer Created Successfully: '+str(newDeveloper.name))
        return redirect("/developers/")
    else:
        return render_template('createDeveloper.html', visibility=1)

# Edit developer
@app.route('/developer/<int:developer_id>/edit', methods=['GET', 'POST'])
def editDeveloper(developer_id):
    if 'username' not in login_session:
        return redirect('/login')
    developer = session.query(Developer).filter_by(id=developer_id).one()
    if login_session['user_id'] != developer.u_id:
        return redirect("/developer/"+str(developer_id)+"/")
    if request.method == 'POST':
        developer.name = request.form['name']
        developer.image = request.form['image']
        developer.description = request.form['description']
        session.add(developer)
        session.commit()
        flash('Developer Edited Successfully: '+str(developer.name))
        return redirect("/developer/"+str(developer.id)+"/")
    else:
        return render_template('editDeveloper.html', developer=developer, visibility=1)

# Delete developer and all their games
@app.route('/developer/<int:developer_id>/delete', methods=['GET', 'POST'])
def deleteDeveloper(developer_id):
    if 'username' not in login_session:
        return redirect('/login')
    developer = session.query(Developer).filter_by(id=developer_id).one()
    if login_session['user_id'] != developer.u_id:
        return redirect("/developer/"+str(developer_id)+"/")
    if request.method == 'POST':
        session.delete(developer)
        games = session.query(Game).filter_by(d_id=developer_id).all()
        for game in games:
            session.delete(game)
        session.commit()
        flash('Developer Deleted Successfully: '+str(developer.name))
        return redirect("/developers/")
    else:
        return render_template('deleteDeveloper.html', developer=developer, visibility=1)

# Create game
@app.route('/developer/<int:developer_id>/game/create', methods=['GET', 'POST'])
def createGame(developer_id):
    if 'username' not in login_session:
        return redirect('/login')
    developer = session.query(Developer).filter_by(id=developer_id).one()
    if login_session['user_id'] != developer.u_id:
        return redirect("/developer/"+str(developer_id)+"/")
    if request.method == 'POST':
        newGame = Game(name=request.form['name'], image=request.form['image'], gameplay=request.form['gameplay'], description=request.form['description'], d_id=developer_id, u_id=login_session['user_id'])
        session.add(newGame)
        session.commit()
        flash('Game Created Successfully: '+str(newGame.name))
        return redirect("/developer/"+str(developer_id))
    else:
        return render_template('createGame.html', developer_id=developer_id, visibility=1)

# Edit game
@app.route('/developer/<int:developer_id>/game/<int:game_id>/edit', methods=['GET', 'POST'])
def editGame(developer_id, game_id):
    if 'username' not in login_session:
        return redirect('/login')
    game = session.query(Game).filter_by(id=game_id).one()
    if login_session['user_id'] != game.u_id:
        return redirect("/developer/"+str(game.d_id)+"/game/"+str(game.id)+"/")
    if request.method == 'POST':
        game.name = request.form['name']
        game.image = request.form['image']
        game.gameplay = request.form['gameplay']
        game.description = request.form['description']
        session.add(game)
        session.commit()
        flash('Game Edited Successfully: '+str(game.name))
        return redirect("/developer/"+str(game.d_id)+"/game/"+str(game.id)+"/")
    else:
        return render_template('editGame.html', developer_id=game.d_id, game=game, visibility=1)

# Delete game
@app.route('/developer/<int:developer_id>/game/<int:game_id>/delete', methods=['GET', 'POST'])
def deleteGame(developer_id, game_id):
    if 'username' not in login_session:
        return redirect('/login')
    game = session.query(Game).filter_by(id=game_id).one()
    if login_session['user_id'] != game.u_id:
        return redirect("/developer/"+str(game.d_id)+"/game/"+str(game.id)+"/")
    if request.method == 'POST':
        session.delete(game)
        session.commit()
        flash('Game Deleted Successfully: '+str(game.name))
        return redirect("/developer/"+str(game.d_id))
    else:
        return render_template('deleteGame.html', game=game, visibility=1)

# Login pages
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state, visibility=checkUserID(login_session))

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    request.get_data()
    code = request.data.decode('utf-8')

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s' % access_token)
    # Submit request, parse response - Python3 compatible
    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # see if user exists, if it doesn't make a new one
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '
    flash("You are now logged in as %s." % login_session['username'])
    return output

def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user

def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

def checkUserID(login_session):
    print login_session
    if 'user_id' not in login_session:
        print False
        return 0
    else:
        return login_session['user_id']

@app.route("/gdisconnect")
def gdisconnect():
    access_token = login_session['access_token']
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % login_session['access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['user_id']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash("Successfully disconnected.")
        return redirect("/")
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response

# Custom error page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.secret_key = "ajsdlfkajfdsjiofad"
    app.debug = True
    app.run(host='0.0.0.0', port=5000)