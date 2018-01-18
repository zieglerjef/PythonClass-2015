# install sqlite from sqlite.org
# pip install sqlalchemy
# pip install pysqlite
import sqlalchemy

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

#Some info about sqlalchemy
print sqlalchemy.__version__

#Connect to the local database, can use :memory: to just try it out in memory
engine = sqlalchemy.create_engine('sqlite:////Users/betuldemirkaya/Desktop/players.db', echo=True)

Base = declarative_base() 

#Define some schemas
class Player(Base):
  __tablename__ = 'players'
  
  #Have an ID column because player attributes (name, etc) are not unique
  id = Column(Integer, primary_key=True)
  name = Column(String)
  number = Column(Integer)
  
  team_id = Column(Integer, ForeignKey("teams.id"))
  
  def __init__(self, name, number, team=None):
    self.name = name
    self.number = number
    self.team = team
    
  def __repr__(self):
    return "<Player('%s', '%s')>" % (self.name, self.number)


class Team(Base):
  __tablename__ = "teams"
  
  id = Column(Integer, primary_key=True)
  name = Column(String)
  players = relationship("Player", backref="team")
  
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "<team('%s')>" % (self.name)
    
# First time create tables


Base.metadata.create_all(engine) 

#See structure of players table:
Player.__table__  

#Create a player
mason = Player("Mason Plumlee", 5)
print str(mason.id)

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

# session.add(mason)
# 
# #Create some more players
# session.add_all([
#   Player("Miles Plumlee", 40),
#   Player("Seth Curry", 30),
#   Player("Austin Rivers", 0),
#   Player("The other Plumlee", 100)
# ])
# 
# #Persist all of this information
# session.commit()
print str(mason.id)

# Some querying
# order the results
for player in session.query(Player).order_by(Player.number):
  print player.number, player.name, player.id
  
#limit the results with offset, might use this for pagination
for player in session.query(Player).order_by(Player.number)[1:3]:
  print player.number, player.name

#Some filters
for player in session.query(Player).filter(Player.name == "Mason Plumlee").order_by(Player.number):
  print player.number, player.name
  
for player in session.query(Player).filter(Player.name != "Mason Plumlee").order_by(Player.number):
  print player.number, player.name
  
for player in session.query(Player).filter(or_(Player.name == "Mason Plumlee", Player.name == "Miles Plumlee")).order_by(Player.number):
  print player.number, player.name
  
for player in session.query(Player).filter(Player.name.like("%Plumlee%")).order_by(Player.number):
  print player.number, player.name

for player in session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number):
  print player.number, player.name

#Results are just lists  
results = session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number)
results.first()

#count is faster than loading all of the objects
session.query(Player).filter(and_(Player.name.like("%Plumlee%"), Player.number > 10)).order_by(Player.number).count()

#how to work with relations
duke = Team('Duke')

players = session.query(Player).all()
mason.team = duke
players[1].team = duke
mason.team.players


#Lets load the two things together
for player, team in session.query(Player, Team).filter(Player.name == "Mason Plumlee").filter(Team.name == "Duke").order_by(Player.number):
  print player.number, player.name, team.name

#equivalently  
for player in session.query(Player).join(Team).filter(Player.name == "Mason Plumlee").filter(Team.name == "Duke").order_by(Player.number):
  print player.number, player.name, player.team.name

#Now some deletion (see SQLAlchemy Cascades for some fun data sanitation)
players
session.query(Player).filter(Player.number == 30).count()
seth = session.query(Player).filter(Player.number == 30).first()
session.delete(seth)
session.query(Player).filter(Player.number == 30).count()
session.query(Player).filter(Player.name.like("%Seth%")).count()
players
players = session.query(Player).all()
players 

#Updating
other_plumlee = players[3]
other_plumlee.name = "Marshall Plumlee"
session.dirty
session.commit()
# 
# How to convert data to csv
players = session.query(Player).all()
for player in players:
  print player.name, player.number, player.team

# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.