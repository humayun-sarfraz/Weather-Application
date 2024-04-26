import sys
import requests
import geocoder
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QHBoxLayout,
)
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 500, 300)  # Increased window size

        # Labels and Input
        self.location_label = QLabel("Location:")
        self.location_input = QLineEdit()
        self.location_input.setPlaceholderText("Type your location or leave blank to use current location")

        # Button and Weather Label
        self.fetch_button = QPushButton()
        self.fetch_button.setIcon(QIcon("search_icon.png"))
        self.fetch_button.setIconSize(QSize(30, 30))  # Fixed icon size
        self.fetch_button.clicked.connect(self.fetch_weather)

        self.weather_label = QLabel()
        self.weather_label.setAlignment(Qt.AlignCenter)  # Center weather information

        # Layout (Main and Horizontal for Icon)
        layout = QVBoxLayout()
        layout.addWidget(self.location_label)
        layout.addWidget(self.location_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.fetch_button)
        button_layout.setAlignment(Qt.AlignRight)
        layout.addLayout(button_layout)

        icon_layout = QHBoxLayout()
        self.weather_icon = QLabel()
        icon_layout.addWidget(self.weather_icon)
        layout.addLayout(icon_layout)

        layout.addWidget(self.weather_label)

        self.setLayout(layout)

    def fetch_weather(self):
        location = self.location_input.text()
        if not location:
            # Get user's current location based on IP address
            current_location = geocoder.ip('me')
            if current_location:
                location = current_location.city
            else:
                QMessageBox.warning(self, "Warning", "Unable to determine your current location.")
                return

        api_key = 'ff2bd97035ac310df4b09d02839398a68'  # Replace with your own API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_description = data['weather'][0]['description']
                temperature = data['main']['temp']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                country = data['sys']['country']

                weather_info = f"Weather in {location}, {country}:\n"
                weather_info += f"Description: {weather_description}\n"
                weather_info += f"Temperature: {temperature}°C\n"
                weather_info += f"Humidity: {humidity}%\n"
                weather_info += f"Wind Speed: {wind_speed} m/s"

                self.weather_label.setText(weather_info)

                # Update weather icon based on description
                self.update_weather_icon(weather_description)
            else:
                self.weather_label.setText("Error fetching weather data")
                self.weather_icon.setPixmap(None)  # Clear icon on error
        except Exception as e:
            self.weather_label.setText(f"An error occurred: {str(e)}")
            self.weather_icon.setPixmap(None)  # Clear icon on error

    def update_weather_icon(self, description):
        icon_path = None
        if "clear" in description:
            icon_path = "./images/sun.png"  # Replace with your path to a sun icon
        elif "clouds" in description:
            icon_path = "./images/clouds.png"  # Replace with your path to a clouds icon
        elif "rain" in description:
            icon_path = "./images/rain.png"  # Replace with your path to a rain icon
        elif "snow" in description:
            icon_path = "./images/snow.png"  # Replace with your path to a snow icon
        elif "thunderstorm" in description:
            icon_path = "./images/thunderstorm.png"  # Replace with your path to a thunderstorm icon
        else:
            icon_path = "./images/sun.png"  # Default to no icon if description doesn't match

        if icon_path:
            pixmap = QPixmap(icon_path)
            pixmap = pixmap.scaled(50, 50, Qt.KeepAspectRatio)  # Resize icon
            self.weather_icon.setPixmap(pixmap)
        else:
            self.weather_icon.setPixmap(None)  # Clear icon if no match

def main():
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
