import requests

def get_nws_forecast(latitude, longitude):
    """
    Fetch the 7-day forecast from the National Weather Service (NWS) API
    for the specified latitude and longitude.
    """
    
    # The base URL to get location-specific metadata (including forecast URL)
    points_url = f"https://api.weather.gov/points/{latitude},{longitude}"
    
    # As requested by NWS, provide a custom User-Agent with contact info
    headers = {
        "User-Agent": "MyWeatherApp/1.0 (contact@example.com)"
    }
    
    try:
        # Step 1: Get metadata for the specified lat/lon
        response_points = requests.get(points_url, headers=headers)
        response_points.raise_for_status()
        data_points = response_points.json()
        
        # Step 2: Extract the forecast URL from the "properties" field
        forecast_url = data_points["properties"]["forecast"]
        
        # Step 3: Get the forecast data
        response_forecast = requests.get(forecast_url, headers=headers)
        response_forecast.raise_for_status()
        data_forecast = response_forecast.json()
        
        # Print out the forecast periods (e.g., "Tonight", "Tomorrow", etc.) and details
        print(f"7-Day Forecast for Seattle (lat={latitude}, lon={longitude})")
        periods = data_forecast["properties"]["periods"]
        for period in periods:
            print(f"{period['name']}: {period['detailedForecast']}")
        
        # Return the full JSON if you need it for further processing
        return data_forecast
    
    except requests.exceptions.RequestException as e:
        print("Error fetching data from the NWS API:", e)
        return None

if __name__ == "__main__":
    # Coordinates for Seattle, WA
    seattle_latitude = 47.6062
    seattle_longitude = -122.3321
    get_nws_forecast(seattle_latitude, seattle_longitude)