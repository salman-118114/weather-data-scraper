import requests
import csv
import os # For checking if the file exists
from datetime import datetime
from config import API_KEY

# Function to fetch weather details for a given city
def get_weather_details(city):
    """Fetches weather data for a city using OpenWeatherMap API."""
    # Using f-string for URL and adding units parameter
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    try:
        #generating the timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        response = requests.get(url)
        response.raise_for_status()  # This handles HTTP errors like 404
        data = response.json()
        
        # Extract relevant weather details into a dictionary
        weather_data = {
            "timestamp": timestamp,
            "city": data.get("name"),
            "country": data["sys"].get("country"),
            "temperature_celsius": data["main"].get("temp"),
            "feels_like_celsius": data["main"].get("feels_like"),
            "min_temp_celsius": data["main"].get("temp_min"),
            "max_temp_celsius": data["main"].get("temp_max"),
            "pressure": data["main"].get("pressure"),
            "humidity": data["main"].get("humidity"),
            "weather": data["weather"][0].get("main"),
            "description": data["weather"][0].get("description"),
            "wind_speed_m_per_s": data["wind"].get("speed"),
            "wind_deg": data["wind"].get("deg"),
            "clouds": data["clouds"].get("all"),
            "visibility": data.get("visibility")
        }
        return weather_data

    except requests.exceptions.HTTPError as e:
        print(f"⚠️ HTTP error occurred. Details: {e}")
        return None
    except requests.exceptions.ConnectionError:
        print("🌐 Network error. Please check your internet connection.")
        return None
    except requests.exceptions.Timeout:
        print("⏳ Request timed out.")
        return None
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        return None

# Main function to run the program
def main():
    file_name = "weather_report.csv"
    # Check if the file already exists to decide whether to write the header
    file_exists = os.path.isfile(file_name)

    while True:
        city_name = input('\nEnter the city name you want to know weather about (or type "exit" to quit): ').strip()
        
        if city_name.lower() == "exit":
            print("👋 Exiting program. Goodbye!")
            break
        
        weather_data = get_weather_details(city_name)

        if weather_data:
            # Use 'with' statement for proper file handling
            with open(file_name, 'a', newline='') as file:
                fieldnames = weather_data.keys()
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                # Write header only if the file did not exist before
                if not file_exists:
                    writer.writeheader()
                    file_exists = True # Set flag to true after writing header
                
                writer.writerow(weather_data)
                print("✅ Weather data saved successfully!")
        else:
            print('No data saved.')

if __name__ == "__main__":
    main()