import requests
import json

def get_weather(lat:str, long:str):
	points_url = f"https://api.weather.gov/points/{lat},{long}"

	headers = {
        "User-Agent": "MyWeatherApp/1.0 (contact@example.com)"
  }
	response = requests.get(points_url, headers=headers)
	weather_api_response = response.json()
	forecast_url = weather_api_response["properties"]["forecast"]

	forecast = requests.get(forecast_url, headers=headers)
	forecast_response = forecast.json()

	properties_forecast_response = forecast_response["properties"]["periods"]
	for item in properties_forecast_response:
		print(f"Item: {item}")
		print("\n")	
	

def main():
	while True:
		lat = input("Enter latitude: ")
		long = input("Enter longitude: ")
		

		get_weather(lat, long)
		print("Tempreture: " + '''tempreture''')
		print("Conditions: " + '''conditions''')
		print("more stuff that id find on a weather app")
		if lat == 'quit':
			print('goodbye')
		break

main()