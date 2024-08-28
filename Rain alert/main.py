import requests
from twilio.rest import Client
import os

api_key = "483b85d1157af3b2b013c6b8b8e10849"
endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
weather_params = {
    "lat": 19.816380,
    "lon": 85.830650,
    "cnt": 4,
    "appid": api_key
}

account_sid = 'AC8bc294ed3130da69d96031e047985739'
auth_token = '8b07ca76f4e77b52c5e1c244418f1e6e'

response = requests.get(endpoint, params=weather_params)
response.raise_for_status()
data = response.json()
weather = data["list"][0]["weather"][0]["id"]

will_rain = False

for hour_data in data["list"]:
    h_data = hour_data["weather"][0]["id"]
    if int(h_data) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="It's going to rain today.Remember to bring an umbrella ",
        to='whatsapp:+919852637240'
    )
    print(message.status)
