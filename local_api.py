import requests

# Send a GET request to the API
r = requests.get("http://127.0.0.1:8000")

# Print the GET response
print("GET Status Code:", r.status_code)
print("GET Response:", r.json())


data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# Send a POST request with the Census data
r = requests.post(
    "http://127.0.0.1:8000/data/",
    json=data
)

# Print the POST response
print("POST Status Code:", r.status_code)
print("POST Response:", r.json())

data = {
    "age": 37,
    "workclass": "Private",
    "fnlgt": 178356,
    "education": "HS-grad",
    "education-num": 10,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "White",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "United-States",
}

# TODO: send a POST using the data above
r = None  # Your code here

# TODO: print the status code
# print()
# TODO: print the result
# print()
