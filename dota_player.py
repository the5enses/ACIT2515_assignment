from abstract_esports_player import AbstractEsportsPlayer
PLAYER_TYPE = "DotaPlayer"


class DotaPlayer(AbstractEsportsPlayer):
    """ Details of a DotaPlayer """
    def __init__(self, id, first_name, last_name, player_name, age, denies, kills, deaths):
        super().__init__(id, first_name, last_name, player_name, age)

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
        return PLAYER_TYPE
