from abstract_esports_player import AbstractEsportsPlayer
from dota_player import DotaPlayer
from league_player import LeaguePlayer

from base import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

ID_COUNTER = 1


class EsportsTeam(Base):
    """ Manager for players """

    __tablename__ = 'esportsteam'

    def __init__(self, db_name):
        """ initialize the attributes of an esports team """

        self._players = []
        self._next_available_id = ID_COUNTER

        if db_name is None or db_name == "":
            raise ValueError("DB Name cannot be undefined")
        engine = create_engine('sqlite:///' + db_name)

        Base.metadata.bind = engine

        self._db_session = sessionmaker(bind=engine)

    def add(self, player_name):
        """ Adds player to roster """
        self._players.append(player_name)

    def get(self, id):
        """ Gets id """
        for x in self._players:
            if x.get_id() == id:
                return x
            else:
                return None

    def get_all(self):
        """ Returns list of all players """
        return self._players

    def get_all_by_type(self, type):
        """ Returns all the players of a type """
        player_type = []

        if type == 'Dota':
            for x in self._players:
                if x.get_type() == 'DotaPlayer':
                        player_type.append(x)

        if type == 'League':
            for x in self._players:
                if x.get_type() == 'LeaguePlayer':
                        player_type.append(x)

    def update(self, player):
        """ Updates list of players """
        for x in self._players:
            if x.get_id() == player.get_id():
                self._players.remove(x)
        self._players.append(player)

    def delete(self, id):
        """ Removes a player from list """
        for x in self._players:
            if x.get_id() == id:
                self._players.remove(x)

    @staticmethod
    def _validate_input_string(display_name, value):
        """ Validates values """

        if value is None:
            raise ValueError(display_name + " cannot be undefined")

        if value == "":
            raise ValueError(display_name + " cannot be left blank")
