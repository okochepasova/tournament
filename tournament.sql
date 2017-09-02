-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
-- 
-- Use the command '\i tournament.sql' to import the whole file into "psql" at
-- once. Use the name 'tournament' for your database.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP DATABASE IF EXISTS tournament;
DROP TABLE IF EXISTS players CASCADE;
DROP TABLE IF EXISTS matches CASCADE;

CREATE DATABASE tournament;
\c tournament

CREATE TABLE players (
    name TEXT,
    id SERIAL PRIMARY KEY
);

CREATE TABLE matches (
    winner INTEGER REFERENCES players(id),
    loser INTEGER REFERENCES players(id),
    PRIMARY KEY (winner, loser)
);

CREATE VIEW total as 
SELECT p.id, count(m.winner) as matches
    FROM players as p LEFT JOIN matches as m
        ON p.id = m.winner OR p.id = m.loser
    GROUP BY p.id;

CREATE VIEW winners as 
SELECT id, count(m.winner) as wins
    FROM players as p LEFT JOIN matches as m
        ON p.id = m.winner
    GROUP BY p.id;

CREATE VIEW standings as 
SELECT p.id, p.name, w.wins, t.matches
    FROM players as p, winners as w, total as t
    WHERE p.id = w.id AND p.id = t.id
    ORDER BY wins DESC;
