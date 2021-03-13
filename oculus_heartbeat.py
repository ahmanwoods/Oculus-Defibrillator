import sqlite3, tempfile, shutil, os, time, requests

def get_oauth_token():
	try:
		#SQLite 3 DB with data used for offline more stored here
		db = os.path.expandvars(r'%APPDATA%\Oculus\sessions\_oaf\\' + 'data.sqlite')
		#DB is locked when Oculus app is open so make a temp copy of the DB to read from
		file, path = tempfile.mkstemp()
		shutil.copy2(db, path)        
		with os.fdopen(file, 'w') as tmp:
			#Connect to the temp DB   
			sqlite = sqlite3.connect(path)
			cur = sqlite.cursor()
			sql_bytes = ''

			#This query should return 1 tuple with the last entry being a byte string, this contains our token.
			for row in cur.execute("SELECT * FROM 'Objects' WHERE hashkey = '__OAF_OFFLINE_DATA_KEY__'"):
				if len(row) > 0:
					for val in row:
						if type(val) is bytes:
							sql_bytes = val
				else:
					raise Exception("No __OAF_OFFLINE_DATA_KEY__ found in db")

			#The token we need is stored in 'last_valid_auth_token'
			if sql_bytes != '':
				start_offset = sql_bytes.find(b'last_valid_auth_token') + 31
			else:
				raise Exception("No byte array values found in __OAF_OFFLINE_DATA_KEY__")

			#Extract the token
			if start_offset != -1:
				delimeter_offset = sql_bytes.find(b'\x1a\x00\x00\x00last_valid_fb_access_token')
				token = sql_bytes[start_offset : delimeter_offset]
				return token.decode('ascii')
			else:
				raise Exception("last_valid_auth_token not found in db")
	except sqlite3.OperationalError:
		print("Error opening sqlite3 db")
	finally:
		#The db may or may not be open depending on the state of the script
		try:
			sqlite.close()
		except:
			pass
		#Always remove the temp file we created
		os.remove(path)

def main():
	#Oculus client Oauth token. 
	oauth = get_oauth_token()
	print("Acquired OAuth Token: {}".format(oauth))
	
	#Heartbeat API URL
	heartbeat_url = "https://graph.oculus.com/user_heartbeat"

	#Oculus App ID. Can be acquired from oculus store at https://www.oculus.com/experiences/rift/appid
	app_id = 1369078409873402 
	#1360938750683878 for Stormland, 1369078409873402 for Echo VR

	#Paramaters for API request. Chance for issues with rich presence but I'm not sure which titles use it.
	params = { 'access_token': oauth, 'current_status' : 'ONLINE', 'app_id_override' : app_id, 'in_vr' : 'true'}

	while True:
		try:
			r = requests.post(heartbeat_url, json=params)
			#200 on successful post
			if r.status_code == 200:
				print("Heartbeat submitted successfully with response: {}".format(r.text))
				time.sleep(10)
			else:
				print("Heartbeat FAILED with status code: {} and response: {}".format(r.status_code, r.text))
				time.sleep(10)
		except Exception as e:
			print(e)
			break
if __name__ == "__main__":
	main()    