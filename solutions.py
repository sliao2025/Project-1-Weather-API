import requests

def get_nws_forecast(latitude, longitude):
    """
    Fetch the 7-day forecast from the National Weather Service (NWS) API
    for the specified latitude and longitude.
    """
    
    points_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    
    headers = {
        "User-Agent": "MyWeatherApp/1.0 (contact@example.com)"
    }
    
    try:
        response_points = requests.get(points_url, headers=headers)
        # response_points.raise_for_status()
        data_points = response_points.json()
        print(data_points)
        forecast_url = data_points["properties"]["forecast"]
        
        response_forecast = requests.get(forecast_url, headers=headers)
        response_forecast.raise_for_status()
        data_forecast = response_forecast.json()
        print(data_forecast)
        
        print(f"\n7-Day Forecast for (lat={latitude}, lon={longitude}):\n")
        periods = data_forecast["properties"]["periods"]
        for period in periods:
            print(f"{period['name']}: {period['detailedForecast']}")
        
        return data_forecast
    
    except requests.exceptions.RequestException as e:
        print("Error fetching data from the NWS API:", e)
        return None

def get_user_coordinates():
    """
    Prompt the user for latitude and longitude and validate input.
    """
    while True:
        try:
            latitude = float(input("Enter latitude: ").strip())
            longitude = float(input("Enter longitude: ").strip())
            return latitude, longitude
        except ValueError:
            print("Invalid input. Please enter valid numerical values for latitude and longitude.")

if __name__ == "__main__":
    latitude, longitude = get_user_coordinates()
    get_nws_forecast(latitude, longitude)