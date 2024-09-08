import requests
from datetime import datetime

USERNAME = "rounakm535"
TOKEN = "isitanapikey"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

GRAPH_ID = "streak2"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Graph",
    "unit": "Codes",
    "type": "int",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


today = datetime.now()
data = today.strftime("%Y%m%d")

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"


pixel_config = {

    "date": data,
    "quantity": "13",
}

# response = requests.post(url=pixel_endpoint, json=pixel_config,headers=headers)
# print(response.text)

update_config = {
    "quantity": "15",
}

pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{data}"

response = requests.put(url=pixel_update_endpoint, json=update_config, headers=headers)
print(response.text)
