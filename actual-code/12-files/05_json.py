import json  # JavaScript Object Notation

print(json.dumps([True, "hello", 1,2,3]))  # converts a Python data structure to JSON

print(json.loads("[true, 1,2,3]"))  # converts a JSON object to Python

with open("data.json") as file:
    json.load(file)
    data = json.loads(file.read())
    print(data['name'])

# pip install numpy pandas matplotlib