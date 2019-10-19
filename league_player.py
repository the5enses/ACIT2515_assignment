from abstract_esports_player import AbstractEsportsPlayer
PLAYER_TYPE = "LeaguePlayer"


class LeaguePlayer(AbstractEsportsPlayer):
    """ Details of a LeaguePlayer"""
    def __init__(self, id, first_name, last_name, player_name, age, num_towers, objectives):
        super().__init__(id, first_name, last_name, player_name, age)

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
        return PLAYER_TYPE
