from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, Developer, Game

engine = create_engine('sqlite:///gamecatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Add user
# user = User(name="Matt Weeks", email="matt.weeks93@gmail.com")
user = User(name="Mtt Wks", email="mtt.wks93@gmail.com")
session.add(user)

# Add Developers and games
dev = Developer(user=user, name="Codemasters Racing", image="http://www.virtualr.net/wp-content/uploads/2012/04/codemastersracing.jpg",
	description="Codemasters Software Company Ltd., or Codemasters Birmingham or CodeMasters (earlier known as Code Masters) is a British video game developer and publisher founded by David Darling and his brother Richard in 1986. Headquartered in Southam, Warwickshire, Codemasters is one of the oldest British game studios, and in 2005 was named the top independent games developer by Develop magazine.")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Dirt 2", image="http://data.1freewallpapers.com/detail/dirt-2.jpg"))
session.add(Game(developer=dev, user=user, name="Dirt 3", image="https://images-eds-ssl.xboxlive.com/image?url=8Oaj9Ryq1G1_p3lLnXlsaZgGzAie6Mnu24_PawYuDYIoH77pJ.X5Z.MqQPibUVTcVL1T87i_j13iJ9H7UxHFvByzHAvxHaYwF8elVl9SxjL3bhHaavB28q1GP_VcMcxH3Uq2549AKyJHSeML5I4vmPA5aWy55I4xdMPDYbTleV1UUniRcl.DXZNGA1ba0eR7r9KcSWpuD_P6B3dPDteOkrylzgaAz2K9McO74cbav9s-&format=jpg"))
session.add(Game(developer=dev, user=user, name="Dirt Rally", image="https://wholesgame.com/wp-content/uploads/Dirt-Rally-Wallpaper-22-04-16.jpg"))
session.add(Game(developer=dev, user=user, name="Dirt Showdown", image="http://www.hdwallpapers.in/thumbs/dirt_showdown-t2.jpg"))
session.add(Game(developer=dev, user=user, name="Grid 2", image="https://www.thenerdfilter.com/wp-content/uploads/2013/06/grid_2_game-wide.jpg"))
session.add(Game(developer=dev, user=user, name="Grid Autosport", image="https://i.ytimg.com/vi/L_dWL72e0XA/maxresdefault.jpg"))

dev = Developer(user=user, name="Crytek", image="http://www.dsogaming.com/wp-content/uploads/2014/05/crytek-logo.jpg")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Crysis", image="http://wallpaper4k.info/wp-content/uploads/2016/01/Crysis-Wallpaper-Design-3D-1280x720.jpg"))
session.add(Game(developer=dev, user=user, name="Crysis Wars", image="http://t.wallpaperweb.org/wallpaper/games/1280x720/38086_1920x1080_1280x720.jpg"))
session.add(Game(developer=dev, user=user, name="Crysis 2", image="http://images4.wikia.nocookie.net/__cb20111005011747/crysis/images/thumb/2/26/Crysis-2-wallpaper-superhero.jpg/1280px-Crysis-2-wallpaper-superhero.jpg"))
session.add(Game(developer=dev, user=user, name="Crysis 3", image="http://idesktopwallpaper.com/wp-content/uploads/2016/01/crysis_3_logo_wallpapers-1280x720.png"))

dev = Developer(user=user, name="Gearbox Software", image="https://i.ytimg.com/vi/PxpMDFErcC0/maxresdefault.jpg",
	description="Gearbox Software, LLC is an American video game development company based in Frisco, Texas. It was established in 1999 by developers from companies such as 3D Realms and Bethesda Softworks, with one of the founders, Randy Pitchford, as CEO. The company initially created expansions for the Valve Software game Half-Life, then ported that game and others to console platforms. In 2005 Gearbox launched its first independent set of games, Brothers in Arms, on console and mobile devices. It became their flagship franchise and spun off a comic book series, television documentary, books, and action figures. Their second original game series Borderlands was released in 2009, and by 2015 had sold over 26 million copies. The company also owns the intellectual property of Duke Nukem and Homeworld.")
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

dev = Developer(user=user, name="Valve", image="http://www.nexxtup.de/wp-content/uploads/2015/04/Valve_logo.png",
	description="Valve Corporation (also known as Valve Software, commonly referred to as Valve) is an American video game developer and digital distribution company headquartered in Bellevue, Washington, United States. Its Luxembourg-based business office subsidiary for European regions, Valve S.a.r.l., was opened in 2012. Founded in 1996 as Valve L.L.C. by former Microsoft employees Gabe Newell and Mike Harrington, the company has developed the critically acclaimed Half-Life, Counter-Strike, Portal, Day of Defeat, Team Fortress, Left 4 Dead video game series, alongside Dota 2. It also developed and maintains Source on which most of its games run, and the software distribution platform Steam, which has led to the Steam Machine, a line of pre-built gaming computers running SteamOS.")
session.add(dev)
session.add(Game(developer=dev, user=user, name="Counter-Strike", image="http://cdn.pcwallart.com/images/counter-strike-wallpaper-terrorists-wallpaper-1.jpg"))
session.add(Game(developer=dev, user=user, name="Dota 2", image="http://www.mmoknight.com/wp-content/uploads/2015/04/Dota-2.jpg"))
session.add(Game(developer=dev, user=user, name="Half-Life 2", image="http://wfiles.brothersoft.com/h/half-life-2-city_159403-1280x720.jpg"))
session.add(Game(developer=dev, user=user, name="Left 4 Dead", image="http://twinfinite.net/wp-content/uploads/2016/01/left-4-dead.jpg"))
session.add(Game(developer=dev, user=user, name="Team Fortress 2", image="http://oyvindhauge.com/blog/wp-content/team-fortress-2_go.jpg"))
session.add(Game(developer=dev, user=user, name="Portal 2", image="https://i.ytimg.com/vi/Fh9Xp-crJE0/maxresdefault.jpg",
	description="Portal 2 is a 2011 first-person puzzle-platform video game developed and published by Valve Corporation. It is the sequel to Portal (2007) and was released on April 19, 2011, for Microsoft Windows, OS X, Linux, PlayStation 3, and Xbox 360. The retail versions of the game are distributed by Electronic Arts while online distribution of the Microsoft Windows, Mac OS X and Linux versions is handled by Valve's content delivery service Steam. Portal 2 was announced on March 5, 2010, following a week-long alternate reality game based on new patches to the original game. Before the game's release on Steam, the company released the Potato Sack, a second multi-week alternate reality game, involving 13 independently developed titles which culminated in a distributed computing spoof to release Portal 2 several hours early.",
	gameplay="https://thesenecatimes.files.wordpress.com/2012/12/portal-2-screenshots-04.jpg"))
session.add(Game(developer=dev, user=user, name="Portal", image="http://cdn.pcwallart.com/images/portal-1-logo-wallpaper-2.jpg"))
session.add(Game(developer=dev, user=user, name="Left 4 Dead 2", image="https://i.ytimg.com/vi/rHaEH7RURJY/maxresdefault.jpg"))
session.add(Game(developer=dev, user=user, name="Counter-Strike: Source", image="http://wallpaper.ultradownloads.com.br/144162_Papel-de-Parede-Counter-Strike--144162_1280x720.jpg"))
session.add(Game(developer=dev, user=user, name="Counter-Strike: Global Offensive", image="http://techfaqs.net/wp-content/uploads/2016/04/CSGO.jpg",
	description="Counter-Strike: Global Offensive (CS:GO) is an online first-person shooter developed by Hidden Path Entertainment and Valve Corporation. It is the fourth game in the main Counter-Strike franchise. Counter-Strike: Global Offensive was released for Microsoft Windows, OS X, Xbox 360, and PlayStation 3 on August 21, 2012. The Linux version was released in September 2014. It features classic content, such as revamped versions of classic maps, as well as brand new maps, characters and game modes. Cross-platform multiplayer was planned between Windows, OS X, Linux, and PlayStation 3 players, but was ultimately limited to Windows, OS X, and Linux because of the differences in update-frequency between systems. The PlayStation 3 version offers three input control methods, which include using either the DualShock 3 controller, PlayStation Move or USB keyboard/mouse.",
	gameplay="http://www.hardwareheaven.com/reviewimages/amd-a4-3400/csgo-screenshot4.jpg"))

session.commit()

print "Database populated."