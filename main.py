import requests
from flask import Flask, json,jsonify,render_template
from json2table import convert

#pull data from api
if __name__ == "__main__":		
	url_players = "https://www.balldontlie.io/api/v1/players"
	r_players = requests.get(url_players)
	response_data_players = r_players.json()

	url_teams = "https://www.balldontlie.io/api/v1/teams"
	r_teams = requests.get(url_teams)
	response_data_teams = r_teams.json()

	

app = Flask(__name__)

@app.route('/index', methods=['GET'])
@app.route('/home', methods=['GET'])
@app.route('/', methods=['GET'])
def home():
  return render_template('index.html')

@app.route('/player', methods=['GET'])
def players():
	return  render_template('players.html')

@app.route('/stats', methods=['GET'])
def stats():
	return  render_template('stats.html')

@app.route('/api', methods=['GET'])
def api():
	return render_template('api.html')

@app.route('/api/players', methods=['GET'])
def api_players():	
	return jsonify(response_data_players)

@app.route('/api/teams', methods=['GET'])
def api_teams():
	return jsonify(response_data_teams)


@app.route('/player/<search>', methods=['GET'])
def get_players(search):
	url_players = f"https://www.balldontlie.io/api/v1/players/?search={search}"
	r_players = requests.get(url_players, params = search)
	response_data_players = r_players.json()
	json_object = response_data_players
	build_direction = "LEFT_TO_RIGHT"
	table_attributes = {"style" : "width:50%"}
	html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
	return html 

@app.route('/teams', methods=['GET'])
def get_teams():
	json_object = response_data_teams
	build_direction = "LEFT_TO_RIGHT"
	table_attributes = {"style" : "width:50%"}
	html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
	return html

@app.route('/stats/<player_id>', methods=['GET'])
# def get_player(player_id):
# 	url_stats_player = f"https://www.balldontlie.io/api/v1/players/{player_id}"
# 	r_stats_player = requests.get(url_stats_player, params = player_id)
# 	response_data_stats_player = r_stats_player.json()
# 	json_object = response_data_stats
# 	build_direction = "LEFT_TO_RIGHT"
# 	table_attributes = {"style" : "width:10%"}
# 	html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
# 	return html 
def get_stats(player_id):
	url_stats = f"https://www.balldontlie.io/api/v1/season_averages?season=2019&player_ids[]={player_id}"
	r_stats = requests.get(url_stats, params = player_id)
	response_data_stats = r_stats.json()
	json_object = response_data_stats
	build_direction = "LEFT_TO_RIGHT"
	table_attributes = {"style" : "width:10%"}
	html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
	return html 




	# teams_table = json2html.convert(json = response_data_teams)
	# your_file= open("filename","w")
	# your_file.write(teams_table)
	# your_file.close()
  # return render_template('teams.html')

# # @app.route(f'/stats/{year}/{player_id}', methods=['GET'])
# # def get_stats():
# url_stats = f"https://www.balldontlie.io/api/v1/season_averages?season={year}>&player_ids[]={player_id}"
# 	r_stats = requests.get(url_stats)
# 	response_data_stats = r_stats.json()
# # 	year = int(year)
# # 	player_id = int(player_id)
# #   	return jsonify(response_data_stats) 


if __name__ == "__main__":
	app.run(debug = True)