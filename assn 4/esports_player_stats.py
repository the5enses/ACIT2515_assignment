class EsportsPlayerStats:
    """ Stats of a Esports Team roster """

    def __init__(self, total_num_players, num_dota_players, num_league_players, avg_age):

        if total_num_players is None or type(total_num_players) != int:
            raise ValueError('Invalid value of players')
        self._total_num_players = total_num_players

        if num_dota_players is None or type(num_dota_players) != int:
            raise ValueError('Invalid value of players')
        self._num_dota_players = num_dota_players

        if num_league_players is None or type(num_league_players) != int:
            raise ValueError('Invalid value of players')
        self._num_league_players = num_league_players

    def get_total_num_players(self):
        return self._total_num_players

    def get_num_dota_players(self):
        return self._num_dota_players

    def get_num_league_players(self):
        return self._num_league_players

    def get_avg_age(self):
        return
