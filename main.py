cities = []

def get_weather(city:str):
	#make API call
	cities.append(city)
	print(cities)


def main():
	while True:
		location = input("Enter a city name: ")

		get_weather(location)
		if location == 'quit':
			print('goodbye')
			break

main()