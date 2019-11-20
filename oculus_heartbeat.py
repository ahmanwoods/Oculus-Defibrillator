import requests
import time

#Oculus client Oauth token. Can be acquired with Fiddler under access_token. Needs HTTPS decryption. 
oauth = ''

#Heartbeat API URL
heartbeat = "https://graph.oculus.com/user_heartbeat?access_token=" + oauth

#Oculus App ID. Can be acquired from oculus store at https://www.oculus.com/experiences/rift/appid
app_id = 1360938750683878 
#1360938750683878 for Stormland, 1369078409873402 for Echo VR

#Paramaters for API request. Chance for issues with rich presence but I'm not sure which titles use it.
params = { 'current_status' : 'ONLINE', 'app_id_override' : app_id, 'in_vr' : 'true'}

while True:
	response = requests.post(heartbeat, params)
	print("Heartbeat submitted")
	#Response should contain current_room_id if working correctly (at least for Stormland)
	print(response.content)
	#Oculus client sends heartbeats every 10 seconds when in game
	time.sleep(10)