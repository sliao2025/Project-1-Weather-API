import requests
import json

def get_weather(lat:str, long:str):
	points_url = f"https://api.weather.gov/points/{lat},{long}"

	response = requests.get(points_url)
	print(response.status_code)
	jsonfile = response.json()
	# dictionary = json.loads(jsonfile)
	keys = jsonfile.keys()
	print(list(keys))
	print(jsonfile["type"])

def main():
	while True:
		lat = input("Enter latitude: ")
		long = input("Enter longitude: ")
		

		get_weather(lat, long)
		print("Tempreture: " + '''tempreture''')
		print("Conditions: " + '''conditions''')
		print("more stuff that id find on a weather app")
		# if location == 'quit':
		# 	print('goodbye')
		# 	break

main()