🌦️ Weather Data Scraper & Analyzer
A Python-based command-line tool that fetches and saves real-time weather data for any given city. This project was built to practice core Python skills, including API interaction, JSON parsing, and file handling.

🎯 Project Goal
The primary objective was to create a robust and user-friendly tool to retrieve weather information from a public API and store it in a structured format (CSV). The tool demonstrates fundamental data collection and preparation skills, which are essential for any data science workflow.

✨ Key Features
API Integration: Fetches weather data by making HTTP requests to the OpenWeatherMap API.

Structured Data Storage: Parses the JSON response and saves key weather metrics (temperature, humidity, wind speed, etc.) to a weather_report.csv file.

Error Handling: Gracefully handles network issues, API errors, and invalid user input.

Timestamping: Automatically adds a timestamp to each record to document when the data was collected.


🛠️ Technologies Used
Python: The core programming language.

requests: A Python library for making HTTP requests to APIs.

csv: Python's built-in module for working with CSV files.

os: Python's built-in module for interacting with the operating system.

datetime: Python's built-in module for handling dates and times.
