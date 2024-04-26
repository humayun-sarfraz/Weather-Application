# Weather Application

This is a simple weather application built using PyQt5 and the OpenWeatherMap API. It allows users to fetch weather information based on a location input or their current location.

## Features

- **Fetch Weather Data**: Users can input a location to fetch weather information or leave it blank to use their current location.
- **Display Weather Information**: The application displays weather information such as temperature, humidity, wind speed, and weather description.
- **Weather Icons**: Weather icons are displayed based on the weather description to visually represent the current weather conditions.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- PyQt5 library (`pip install PyQt5`)
- Requests library (`pip install requests`)
- Geocoder library (`pip install geocoder`)

## Usage

1. Clone or download the repository to your local machine.
2. Install the required dependencies as mentioned in the prerequisites.
3. Run the `weather_app.py` file using Python.
4. Enter a location in the input field and click the "Fetch" button to get weather information. Alternatively, leave the input blank to use your current location.
5. Weather information will be displayed along with a weather icon representing the current weather conditions.

## Configuration

To use the application, you need to obtain an API key from OpenWeatherMap:

1. Sign up on [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get your API key.
2. Replace the placeholder `api_key` variable in the `weather_app.py` file with your API key.

## Weather Icons

Weather icons used in the application are provided under the `images` directory. You can replace these icons with your preferred icons or customize them according to your requirements.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
