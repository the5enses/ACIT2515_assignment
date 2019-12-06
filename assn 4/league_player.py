from abstract_esports_player import AbstractEsportsPlayer
from sqlalchemy import *
from base import Base


class LeaguePlayer(Base):
    """ Details of a LeaguePlayer"""

    PLAYER_TYPE = "LeaguePlayer"

    __tablename__ = 'leagueplayer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    player_name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)
    num_towers = Column(Integer, nullable=False)
    objectives = Column(Integer, nullable=False)
    type = Column(String(20), nullable=False)

    def __init__(self, id, first_name, last_name, player_name, age, num_towers, objectives):
        super().__init__(id, first_name, last_name, player_name, age, self.PLAYER_TYPE)

        LeaguePlayer._validate_input_integer('Number of towers destroyed', num_towers)
        self._num_towers = num_towers

        LeaguePlayer._validate_input_integer('Number of objectives completed', objectives)
        self._objectives = objectives

    def get_num_towers(self):
        """ Returns number of towers destroyed """
        return self._num_towers

    def get_num_objectives(self):
        """ Returns number of objectives completed """
        return self._objectives

    def get_details(self):
        """ Returns details of a League player"""
        return "%s (%s %s, age %d) has destroyed %d towers and completed %d objectives." \
               % (self.get_player_name(), self.get_first_name(), self.get_last_name(), self.get_age(),
                  self.get_num_towers(), self.get_num_objectives())

    def get_type(self):
        """ Returns the player type """
        return self.__class__.__name__

    def to_dict(self):
        dict = {}

        dict["id"] = self._id
        dict["first_name"] = self._first_name
        dict["last_name"] = self._last_name
        dict["player_name"] = self._player_name
        dict["age"] = self._age
        dict["num_towers"] = self._num_towers
        dict["objectives"] = self._objectives

        return dict

    @staticmethod
    def _validate_input_integer(display_name, value):
        """Private helper to validate values"""

        if isinstance(value, int) is False:
            raise ValueError(display_name + " must be integer.")
