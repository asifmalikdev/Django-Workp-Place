import json
import requests

URL = "http://127.0.0.1:8000/crud/stuCreateExternal/"
data = {
    "name": "kashif",
    "roll": 5762,
    "city": "bwp"
}
def function_call(data):
    json_data = json.dumps(data)

    try:
        r = requests.post(url=URL, data=json_data, headers={"Content-Type": "application/json"})
        print("Status Code:", r.status_code)
        print("Response Text:", r.text)
        try:
            response_data = r.json()
            print("JSON Response:", response_data)
        except ValueError:
            print("Response is not JSON.")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

# function_call(data)













