import requests
import json

def get_weather(lat:str, long:str):
	points_url = f"https://api.weather.gov/points/{lat},{long}"

	headers = {
        "User-Agent": "MyWeatherApp/1.0 (contact@example.com)"
  }
	response = requests.get(points_url, headers=headers)
	print(response.json())

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