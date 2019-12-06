from flask import Flask, request
from esports_team import EsportsTeam
from dota_player import DotaPlayer
from league_player import LeaguePlayer
import json

app = Flask(__name__)
ESPORTS_PLAYERS_DB = "esports_players.sqlite"
team = EsportsTeam(ESPORTS_PLAYERS_DB)


@app.route('/esports_team/players', methods=['POST'])
def add_player():

    content = request.json

    try:
        if content["type"] == "LeaguePlayer":
            age = int(content["age"])
            num_towers = int(content["num_towers"])
            objectives = int(content["objectives"])
            player = LeaguePlayer(content["id"], content["first_name"], content["last_name"], content["player_name"],
                                  age, num_towers, objectives)

        elif content["type"] == "DotaPlayer":
            age = int(content["age"])
            denies = int(content["denies"])
            kills = int(content["kills"])
            deaths = int(content["deaths"])
            player = DotaPlayer(content["id"], content["first_name"], content["last_name"],
                                content["player_name"], age, denies, kills, deaths)

        player_id = team.add(player)

        response = app.response_class(
                status=200,
                response=str(player_id)
            )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=400,
            mimetype="application/json"
        )

    return response


@app.route('/esports_team/players/<int:id>', methods=['PUT'])
def update_player(id):
    content = request.json

    if id <= 0:
        response = app.response_class(
            status=400
        )
        return response

    try:
        if content["type"] == "LeaguePlayer":
            age = int(content["age"])
            num_towers = int(content["num_towers"])
            objectives = int(content["objectives"])
            player = LeaguePlayer(content["id"], content["first_name"], content["last_name"], content["player_name"],
                                  age, num_towers, objectives)

        elif content["type"] == "DotaPlayer":
            age = int(content["age"])
            denies = int(content["denies"])
            kills = int(content["kills"])
            deaths = int(content["deaths"])
            player = DotaPlayer(content["id"], content["first_name"], content["last_name"],
                                content["player_name"], age, denies, kills, deaths)

        team.update(player)

        response = app.response_class(
            status=200,
        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404,
            mimetype="application/json"
        )

    return response


@app.route('/esports_team/players/<int:id>', methods=['DELETE'])
def delete_player(id):

    if id <= 0:
        response = app.response_class(
            status=400
        )
        return response

    try:
        team.delete(id)
        response = app.response_class(
                status=200
        )

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )

    return response


@app.route('/esports_team/players/<int:id>', methods=['GET'])
def get_player(id):

    if id <= 0:
        response = app.response_class(
            response=400
        )
        return response

    try:
        player = team.get(id)

        response = app.response_class(
            status=200,
            response=json.dumps(player.to_dict()),
            mimetype='application/json'
        )
        return response

    except ValueError as e:
        response = app.response_class(
            response=str(e),
            status=404
        )
    return response


@app.route('/esports_team/players/all', methods=['GET'])
def get_all_players():

    player_list = team.get_all()
    players = []

    for player in player_list:
        players.append(player.to_dict())

    response = app.response_class(
        status=200,
        response=json.dumps(players),
        mimetype='application/json'

    )

    return response


@app.route('/esports_team/players/all/<type>', methods=['GET'])
def get_all_players_of_type(type):

    try:
        players = []

        for player in team.get_all_by_type(type):
            players.append(player.to_dict())

        response = app.response_class(
            response=json.dumps(players),
            status=200
        )
        return response

    except ValueError:
        response = app.response_class(
            response="type not supported",
            status=400,
            mimetype='application/json'
        )
        return response


if __name__ == "__main__":
    app.run(debug=True)
