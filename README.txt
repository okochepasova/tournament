Tournament Planner - 01/30/2017

===============================================================================
    Introduction
===============================================================================
This project is a Python module that uses the PostgreSQL database to keep 
track of players and matches in a game tournament.

The game tournament uses the Swiss system for pairing up players in each 
round: players are not eliminated, and each player is be paired with another 
player with the same number of wins, or as close as possible.


-------------------------------------------------------------------------------
    Installation
-------------------------------------------------------------------------------
Make sure you have Git, Vagrant, VirtualBox and Python installed.

Right click on the empty space inside your folder and choose "Git Bash Here". 
Start up the Virtual Machine and change to the tournament directory.
  $ vagrant up
  $ vagrant ssh
  ~$ cd /vagrant/tournament

Please note that your path may differ. In that case, start at the vagrant 
directory and use "ls" to view all available items. Search until you find the 
correct path.

Run PSQL. To create the database and connect to it, use the commands: 
  vagrant => \i tournament.sql;
  vagrant => \c tournament;
  tournament =>
Exit PSQL "\q".

Type in "python tournament_test.py". In order to reset your database: enter 
into PSQL and repeat the steps from above.

-------------------------------------------------------------------------------
    Copyright
-------------------------------------------------------------------------------
The starter code was provided by Udacity. All changes where made by me.
