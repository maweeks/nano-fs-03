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
session.add(Game(developer=dev, user=user, name="Dirt 2", image="http://data.1freewallpapers.com/detail/dirt-2.jpg"))
session.add(Game(developer=dev, user=user, name="Dirt 3", image="https://wallpaperscraft.com/image/dirt_3_name_game_font_race_15814_1280x720.jpg"))
session.add(Game(developer=dev, user=user, name="Dirt Rally", image="https://wholesgame.com/wp-content/uploads/Dirt-Rally-Wallpaper-22-04-16.jpg"))
session.add(Game(developer=dev, user=user, name="Dirt Showdown", image="http://www.hdwallpapers.in/thumbs/dirt_showdown-t2.jpg"))
session.add(Game(developer=dev, user=user, name="Grid 2", image="http://data.1freewallpapers.com/detail/grid-2-logo.jpg"))
session.add(Game(developer=dev, user=user, name="Grid Autosport", image="https://i.ytimg.com/vi/L_dWL72e0XA/maxresdefault.jpg"))

dev = Developer(user=user, name="Crytek", image="http://www.dsogaming.com/wp-content/uploads/2014/05/crytek-logo.jpg")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Crysis", image="http://wallpaper4k.info/wp-content/uploads/2016/01/Crysis-Wallpaper-Design-3D-1280x720.jpg"))
session.add(Game(developer=dev, user=user, name="Crysis Wars", image="http://t.wallpaperweb.org/wallpaper/games/1280x720/38086_1920x1080_1280x720.jpg"))
session.add(Game(developer=dev, user=user, name="Crysis 2", image="http://images4.wikia.nocookie.net/__cb20111005011747/crysis/images/thumb/2/26/Crysis-2-wallpaper-superhero.jpg/1280px-Crysis-2-wallpaper-superhero.jpg"))
session.add(Game(developer=dev, user=user, name="Crysis 3", image="http://idesktopwallpaper.com/wp-content/uploads/2016/01/crysis_3_logo_wallpapers-1280x720.png"))

dev = Developer(user=user, name="Gearbox Software", image="https://i.ytimg.com/vi/PxpMDFErcC0/maxresdefault.jpg")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Borderlands", image="https://www.feralinteractive.com/data/games/borderlandsgoty/images/media/desktops/psycho_1680.jpg"))
session.add(Game(developer=dev, user=user, name="Borderlands 2", image="http://img00.deviantart.net/5bf9/i/2015/247/d/9/borderlands_2_wallpaper_1920x1080_by_roxelp-d98cyon.png"))
session.add(Game(developer=dev, user=user, name="Borderlands: The Pre-Sequel", image="https://wallpaperscraft.com/image/borderlands_the_pre_sequel_2014_2k_australia_100144_1280x720.jpg"))

dev = Developer(user=user, name="Hidden Path Entertainment", image="http://www.zebrapartners.net/wp-content/uploads/2012/11/HiddenPathLogo1.png")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Defense Grid: The Awakening", image="http://www.mobygames.com/images/shots/l/433129-defense-grid-the-awakening-xbox-360-screenshot-title-screen.jpg"))
session.add(Game(developer=dev, user=user, name="Defense Grid 2", image="http://ihdwallpapers.com/thumbs/2014/10/23/defense_grid_2_game-t2.jpg"))

dev = Developer(user=user, name="Ubisoft", image="http://twinfinite.net/wp-content/uploads/2016/02/ubisoft-logo.jpg")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Assassin's Creed", image="http://www.push-start.co.uk/wp-content/uploads/2014/08/assassins-creed-logo.jpg"))
session.add(Game(developer=dev, user=user, name="Assassin's Creed II", image="https://upload.wikimedia.org/wikipedia/fr/archive/0/04/20100513155650!Assassin's_Creed_II_logo.png"))
session.add(Game(developer=dev, user=user, name="Assassin's Creed Unity", image="http://hambook.herobo.com/gal/AC/AC-Unity-logo-hd-wallpaper.jpg"))
session.add(Game(developer=dev, user=user, name="Driver San Francisco", image="https://www.expatads.com/adpics1/2016/4/XGamer-Technologies-Driver-San-Francisco-COMPUTER-Game-571d3ee44e8e9531fb1c.jpg"))
session.add(Game(developer=dev, user=user, name="The Crew", image="http://static2.cdn.ubi.com/emea/gamesites/TheCrew/asset/wallpapers/THECREW_Wallpaper_1280x720.jpg"))

dev = Developer(user=user, name="Valve", image="http://www.nexxtup.de/wp-content/uploads/2015/04/Valve_logo.png")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Counter-Strike", image="http://cdn.pcwallart.com/images/counter-strike-wallpaper-terrorists-wallpaper-1.jpg"))
session.add(Game(developer=dev, user=user, name="Dota 2", image="http://www.mmoknight.com/wp-content/uploads/2015/04/Dota-2.jpg"))
session.add(Game(developer=dev, user=user, name="Half-Life 2", image="http://wfiles.brothersoft.com/h/half-life-2-city_159403-1280x720.jpg"))
session.add(Game(developer=dev, user=user, name="Left 4 Dead", image="http://twinfinite.net/wp-content/uploads/2016/01/left-4-dead.jpg"))
session.add(Game(developer=dev, user=user, name="Team Fortress 2", image="http://oyvindhauge.com/blog/wp-content/team-fortress-2_go.jpg"))
session.add(Game(developer=dev, user=user, name="Portal 2", image="https://i.ytimg.com/vi/Fh9Xp-crJE0/maxresdefault.jpg"))
session.add(Game(developer=dev, user=user, name="Portal", image="http://cdn.pcwallart.com/images/portal-1-logo-wallpaper-2.jpg"))
# session.add(Game(developer=dev, user=user, name="Left 4 Dead 2"))
session.add(Game(developer=dev, user=user, name="Left 4 Dead 2", image="https://i.ytimg.com/vi/rHaEH7RURJY/maxresdefault.jpg"))
session.add(Game(developer=dev, user=user, name="Counter-Strike: Source", image="http://wallpaper.ultradownloads.com.br/144162_Papel-de-Parede-Counter-Strike--144162_1280x720.jpg"))
session.add(Game(developer=dev, user=user, name="Counter-Strike: Global Offensive", image="http://techfaqs.net/wp-content/uploads/2016/04/CSGO.jpg"))

session.commit()

print "Database populated."