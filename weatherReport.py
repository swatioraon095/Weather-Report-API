import requests
from datetime import datetime
 
# Enter your API key
api_key = "write your api here"
 
api_url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name : ")
 
#for the complete url of the location
complete_url = api_url + "appid=" + api_key + "&q=" + city
response = requests.get(complete_url)
data = response.json()

# Check the value of "cod" key that is equal to "404" which means city is found otherwise city is not found
  

current_temperature = data["main"]["temp"]
 
current_pressure = data["main"]["pressure"]

current_humidity = data["main"]["humidity"]
 
z = data["weather"]
 
current_weather= z[0]["description"]

date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
print("\n\n")

print ("------------- Today's ({}) Weather in {}".format(date_time,city.upper()) + "-------------------")
print("\n===================================ooooooooooooooooo=================================")
print("\n\nTemperature (in kelvin) = " + str(current_temperature) + "K")
print("\n Current Atmospheric Pressure (in hPa unit) = " + str(current_pressure)) 
print("\n Current Humidity= " + str(current_humidity) + "%")
print("\n Current Weather Description = " + str(current_weather))
print("\n\n--------------------------------xxxxxxxxxxxxxxxxxxx--------------------------------")
 
