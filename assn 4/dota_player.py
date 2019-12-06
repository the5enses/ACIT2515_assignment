from abstract_esports_player import AbstractEsportsPlayer
from sqlalchemy import *
from base import Base


class DotaPlayer(Base):
    """ Details of a DotaPlayer """

    PLAYER_TYPE = "DotaPlayer"

    __tablename__ = 'dotaplayer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    player_name = Column(String(30), nullable=False)
    age = Column(Integer, nullable=False)
    denies = Column(Integer, nullable=False)
    kills = Column(Integer, nullable=False)
    deaths = Column(Integer, nullable=False)
    type = Column(String(20), nullable=False)

    def __init__(self, id, first_name, last_name, player_name, age, denies, kills, deaths):
        super().__init__(id, first_name, last_name, player_name, age, self.PLAYER_TYPE)

        DotaPlayer._validate_input_integer('Number of denies', denies)
        self._denies = denies

        DotaPlayer._validate_input_integer('Number of kills', kills)
        self._kills = kills

        DotaPlayer._validate_input_integer('Number of deaths', deaths)
        self._deaths = deaths

    def get_num_denies(self):
        """ Returns number of denies """
        return self._denies

    def get_num_kills(self):
        """ Returns number of kills """
        return self._kills

    def get_num_deaths(self):
        """ Returns number of deaths """
        return self._deaths

    def get_details(self):
        """ Returns details of a Dota player """
        return "%s (%s %s, age %d) has %d denies, %d kills, and %d deaths." \
               % (self.get_player_name(), self.get_first_name(), self.get_last_name(), self.get_age(),
                  self.get_num_denies(), self.get_num_kills(), self.get_num_deaths())

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
        dict["denies"] = self._denies
        dict["kills"] = self._kills
        dict["deaths"] = self._deaths

        return dict

    @staticmethod
    def _validate_input_integer(display_name, value):
        """Private helper to validate values"""

        if isinstance(value, int) is False:
            raise ValueError(display_name + " must be integer.")
