Fullstack Nano 3 - Game Catalog
=======================================
_Forked from udacity/fullstack-nanodegree-vm_

Setup(Mac):
-----------

1. Install [VirtualBox](https://www.virtualbox.org) and [Vagrant](http://vagrantup.com/)

2. Clone this repository.

  ```
  git clone https://github.com/maweeks/nano-fs-03.git
  ```

3. Open the terminal application

4. Navigate inside the cloned repository, into the vagrant folder.

	```
	cd [REPOSITORY_LOCATION]/nano-fs-02/vagrant
	````

5. Start up and connect to the vagrant machine using the following command:

  ```
  vagrant up; vagrant ssh;
  ```

6. Set up the database and run the web server using the following command:

  ```
  cd /vagrant/catalog/; rm gamecatalog.db; python database_setup.py; python database_populate.py; python application.py;
  ```

_The application is now set up to be used._

7. Visit the following address to use the application.

 ```
 localhost:5000
 ```

JSON endpoints:
The following JSON endpoints are available:

 ```
 /JSON
 /developers/JSON
 /developer/<int:developer_id>/JSON
 /developer/<int:developer_id>/games/JSON
 /developer/<int:developer_id>/game/<int:game_id>/JSON
 /games
 ```

Data sources:
-------------
All images have been aquired online, a full list is located in /vagrant/catalog/database_populate.py

All descriptions have been sourced from wikipedia.
