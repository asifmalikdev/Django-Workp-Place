import json
import requests


URL = "http://127.0.0.1:8000/api4/student_api/"
def get_data(id=None):
    data = {}
    print("id : ",id)
    if id is not None:
        data['id'] = id
    print("id : ",id)
    try:
        print('id :', id)
        r = requests.get(url=URL, params=data)
        r.raise_for_status()  # Raise error if not 200 OK
        try:
            data = r.json()
            print(data, "asif")
        except ValueError:
            print("Response is not valid JSON:", r.text)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)


# get_data(2)



#=========================================================
def add_student_external(data=None ):

    try:
        print(data)
        r = requests.post(url=URL, json=data, headers={"Content-Type": "application/json"})
        print("Status Code:", r.status_code)
        print("Response Text:", r.text)
        try:
            response_data = r.json()
            print("JSON Response:", response_data)
        except ValueError:
            print("Response is not JSON.")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

data = {
    "name": "muhammad ali",
    "roll": 68,
    "city": "bwp"
}
# add_student_external(data)

#===============================================================


# Function to perform a partial update (PATCH request)
def partial_update_student_external(id, data):
    try:
        r = requests.patch(url=URL, json={"id": id, **data}, headers={"Content-Type": "application/json"})
        print("Status Code:", r.status_code)
        print("Response Text:", r.text)
        try:
            response_data = r.json()
            print("JSON Response:", response_data)
        except ValueError:
            print("Response is not JSON")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

update_data = {
    "name": "Nawaz Shareef",  # Only updating the name field
    "city": "London"  # Only updating the city field
}

# partial_update_student_external(17, update_data)


#----------------------------------------------------------------
# update one student data completely

def update_student():
    data = {
        'id': 1,
        'name': "aqib sb",
        'roll': 768,
        'city': 'ape'
    }
    headers = {'Content-Type': 'application/json'}
    try:
        r = requests.put(url = URL , headers=headers,  data = json.dumps(data))
        print(r.text)
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

# update_student()


def delete_data():
    data ={
        'id': 4
    }
    headers = {'content-Type': 'application/json'}
    json_data = json.dumps(data)
    try:
        r = requests.delete(url=URL, headers=headers, data = json_data )
        print(r.text)
    except requests.exceptions.RequestException as e:
        print('request failed', e)

delete_data()


URL = "http://127.0.0.1:8000/api/student_create/"
def student_create(data):
    json_data = json.dumps(data)
    r = requests.post(url = URL, data = json_data )
    # r = r.json()
    print("response:", r.status_code, r.text)


data = {
    "name": "bilal bhatti",
    "roll": 988,
    "city": "Multan"
}
# student_create(data)

