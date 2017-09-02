#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    db = psycopg2.connect("dbname=tournament")
    cursor = db.cursor()
    return db, cursor


def deleteMatches():
    """Remove all the match records from the database."""
    # Openinging
    db, c = connect()

    # Body
    # https://www.postgresql.org/docs/9.3/static/sql-truncate.html
    query = "TRUNCATE matches;"
    c.execute(query)
    db.commit()

    # Closing
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    # Openinging
    db, c = connect()

    # Body
    query = "TRUNCATE players;"
    c.execute(query)
    db.commit()

    # Closing
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    # Openinging
    db, c = connect()

    # Body
    query = "SELECT count(*) as num FROM players;"
    c.execute(query)
    num = c.fetchall()

    # Closing
    db.close()
    return int(num[0][0])


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    # Openinging
    db, c = connect()

    # Body
    query = "INSERT INTO players (name) VALUES (%s);"
    param = (name,)
    c.execute(query, param)
    db.commit()

    # Closing
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    # Openinging
    db, c = connect()

    # Body
    query = "SELECT * FROM standings;"
    c.execute(query)

    list = [(int(row[0]), str(row[1]), int(row[2]), int(row[3])) 
             for row in c.fetchall()]

    # Closing
    db.close()
    return list;


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    # Openinging
    db, c = connect()

    # Body
    if str(winner).isdigit() and str(loser).isdigit():
        query = "INSERT INTO matches VALUES (%s);"
        param = winner+', '+loser
        c.execute(query, param))
        db.commit()

    # Closing
    db.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    # Variables
    record = playerStandings()

    # Openinging
    db, c = connect()

    # Body
    list = [(record[i][0], record[i][1], record[i+1][0], record[i+1][1])
             for i in range(0, len(record), 2)]

    # Closing
    db.close()
    return list
