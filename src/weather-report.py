# ------------------------------------------------------------------------------
# EXERCISE WEATHER REPORT
# ------------------------------------------------------------------------------
# • Write code that creates a sentence containing the information of the days
#   weather and peak temperature.
# • The weather information will be provided from the weather station as a
#   variable of type string such as "sunny" or "clouded" and a temperature
#   value of type int.
# • The complete sentence should be printed to the console.
# ------------------------------------------------------------------------------


# Define variables from weather station

weather_today = "cloudy"
temperature_today = 20


# Create sentence

# sentence = "Today it's sunny and the temperature is 33°C"
empty_sentence = "Today it's %s and the temperature is %d °C"
weather_sentence = empty_sentence % (weather_today, temperature_today)

# Create output

print(weather_sentence)
