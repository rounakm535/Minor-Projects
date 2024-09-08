import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 175
AGE = 21

APP_ID = "5b34ff54"
API_KEY = "b0a22ae456607d9b6c3c617b354d72bb"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/369d8aee12a0a1dc369d6d93e0bfdc18/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=nutritionix_headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety API Authentication
# SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
# SHEETY_USERNAME = "rounakm535"
# SHEETY_PASSWORD = "Rounak@1879"
#
# sheety_headers = {
#     "Authorization": f"Basic {SHEETY_TOKEN}"
# }

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {

            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            "rounakm535",
        "Rounak@1879",
        )
    )
