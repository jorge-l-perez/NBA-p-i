#NBA-p-i
NBA-p-i is a simple web server built using the flask package for the WPP General Assembly course final presentation.

#Description
NBA-p-i has team and player data for all current and former NBA players. The server has an html table to display current teams and search functionality for basic player data. Using player data mentioned, the server allows for the pulling of season average data. There are also two API JSON endpoints on the server, one for teams and the other for players.

#Installation
The main.py utilizes the flask package, requests, and json2table for visual creation. 

#Usage
Player Search - [BASE_URL]/player/[insert_search_here] allows the user to search the server for a specific player. Searches are string only and can include spaces, though the URL will be auto-corrected to include "%20"

Stat Search - [BASE_URL]/stats/[insert_player_id_here] allows the user to pull season averages for the latest season for all major statistics. Player IDs can be gathered from the Player Search above. All Stat Searches must be for one player at a time.

#Support
Feel free to reach out to jlperez6234@gmail.com with any questions or comments.

#Roadmap
1. Incorporate clickable JSON/HTML to show players on Teams and player statistics in a more user friendly way.
2. Allow functionaly to include player data alongside stat data.
3. Add headers to every route. 
4. Integrate server with other prominent NBA packages like NBApy.

#Acknowledgements
I would like to thank all the TAs and Taq for guiding us through the challenges of Python over the last months. Data credited to balldontlie.io API.

