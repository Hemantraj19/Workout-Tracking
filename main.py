import requests
from datetime import datetime

APP_ID = "your app id"
API_KEY = "your api key"
BEARER_TOKEN = "your bearer token"

host_domain = "https://trackapi.nutritionix.com"

nlp_exercise_endpoint = f"{host_domain}/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": input("Tell me about the exercise you did: "),
}

response = requests.post(url=nlp_exercise_endpoint, json=parameters, headers=headers)
exercise_data = response.json()

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().time().strftime("%X")

sheety_endpoint = "yours sheet endpoint"
headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}

for exercise in exercise_data['exercises']:
    current_exercise = exercise['name']
    duration = str(exercise['duration_min'])
    calories = str(exercise['nf_calories'])
    sheety_parameter = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": current_exercise.title(),
            "duration":  duration,
            "calories": calories,
        }
    }
    sheety_response = requests.post(url=sheety_endpoint, json=sheety_parameter, headers=headers)
    print(sheety_response.text)

