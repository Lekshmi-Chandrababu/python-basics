# json_handling.py

import json

data = {
    "name": "Lekshmi",
    "age": 21,
    "course": "MCA"
}

json_data = json.dumps(data)
print("JSON String:", json_data)

python_data = json.loads(json_data)
print("Python dict:", python_data)
