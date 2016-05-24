from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Developer, Game

engine = create_engine('sqlite:///gamecatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add user
user = User(name="Matt Weeks", email="matt.weeks93@gmail.com")
session.add(user)

# Add Developers and games
dev = Developer(user=user, name="Codemasters Racing", image="http://www.virtualr.net/wp-content/uploads/2012/04/codemastersracing.jpg")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Dirt 2"))
session.add(Game(developer=dev, user=user, name="Dirt 3"))
session.add(Game(developer=dev, user=user, name="Dirt Rally"))
session.add(Game(developer=dev, user=user, name="Dirt Showdown"))
session.add(Game(developer=dev, user=user, name="Grid"))
session.add(Game(developer=dev, user=user, name="Grid 2"))
session.add(Game(developer=dev, user=user, name="Grid Autosport"))

dev = Developer(user=user, name="Crytek", image="http://www.dsogaming.com/wp-content/uploads/2014/05/crytek-logo.jpg")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Crysis"))
session.add(Game(developer=dev, user=user, name="Crysis Warhead"))
session.add(Game(developer=dev, user=user, name="Crysis Wars"))
session.add(Game(developer=dev, user=user, name="Crysis 2"))
session.add(Game(developer=dev, user=user, name="Crysis 3"))

dev = Developer(user=user, name="Gearbox Software", image="https://i.ytimg.com/vi/PxpMDFErcC0/maxresdefault.jpg")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Borderlands"))
session.add(Game(developer=dev, user=user, name="Borderlands 2"))
session.add(Game(developer=dev, user=user, name="Borderlands: The Pre-Sequel"))

dev = Developer(user=user, name="Hidden Path Entertainment", image="http://www.zebrapartners.net/wp-content/uploads/2012/11/HiddenPathLogo1.png")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Defense Grid: The Awakening"))
session.add(Game(developer=dev, user=user, name="Defense Grid 2"))

# dev = Developer(user=user, name="Redlynx", image="")
# session.add(dev)
# session.add(Game(developer=dev, user=user, name="Trials 2: Second Edition"))
# session.add(Game(developer=dev, user=user, name="Trials Evolution"))
# session.add(Game(developer=dev, user=user, name="Trials Fusion"))

dev = Developer(user=user, name="Ubisoft", image="http://twinfinite.net/wp-content/uploads/2016/02/ubisoft-logo.jpg")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Assassin's Creed"))
session.add(Game(developer=dev, user=user, name="Assassin's Creed II"))
session.add(Game(developer=dev, user=user, name="Assassin's Creed Revelations"))
session.add(Game(developer=dev, user=user, name="Driver San Francisco"))
session.add(Game(developer=dev, user=user, name="The Crew"))

dev = Developer(user=user, name="Valve", image="http://www.nexxtup.de/wp-content/uploads/2015/04/Valve_logo.png")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Counter-Strike"))
session.add(Game(developer=dev, user=user, name="Dota 2"))
session.add(Game(developer=dev, user=user, name="Half-Life"))
session.add(Game(developer=dev, user=user, name="Half-Life 2"))
session.add(Game(developer=dev, user=user, name="Half-Life 2: Episode One"))
session.add(Game(developer=dev, user=user, name="Half-Life 2: Episode Two"))
session.add(Game(developer=dev, user=user, name="Half-Life 2: Lost Coast"))
session.add(Game(developer=dev, user=user, name="Left 4 Dead"))
session.add(Game(developer=dev, user=user, name="Ricochet"))
session.add(Game(developer=dev, user=user, name="Team Fortress Classic"))
session.add(Game(developer=dev, user=user, name="Team Fortress 2", image="http://oyvindhauge.com/blog/wp-content/team-fortress-2_go.jpg"))
session.add(Game(developer=dev, user=user, name="Portal 2", image="https://i.ytimg.com/vi/Fh9Xp-crJE0/maxresdefault.jpg"))
session.add(Game(developer=dev, user=user, name="Portal", image="http://cdn.pcwallart.com/images/portal-1-logo-wallpaper-2.jpg"))
session.add(Game(developer=dev, user=user, name="Left 4 Dead 2", image="https://i.ytimg.com/vi/rHaEH7RURJY/maxresdefault.jpg"))
session.add(Game(developer=dev, user=user, name="Counter-Strike: Source", image="http://wallpaper.ultradownloads.com.br/144162_Papel-de-Parede-Counter-Strike--144162_1280x720.jpg"))
session.add(Game(developer=dev, user=user, name="Counter-Strike: Global Offensive", image="http://techfaqs.net/wp-content/uploads/2016/04/CSGO.jpg"))

session.commit()

print "Database populated."