import requests, json

# Define the base URL of your Django API
base_url = "http://localhost:8000/api/person/"  # Replace with your API's URL

create_url = "http://127.0.0.1:8000/api/person/create/"
detail_url = "http://127.0.0.1:8000/api/person/detail/"
update_url = "http://127.0.0.1:8000/api/person/update/"
delete_url = "http://127.0.0.1:8000/api/person/delete/"
# Headers for JSON content
headers = {"Content-Type": "application/json", }

# Function to pretty print JSON responses
def pretty_print(response):
    print(f"Status Code: {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=4))
    except ValueError:
        print(response.text)

# Create a new person (POST request)
new_person_data = {
    "name": "JPcodes"
}
response = requests.post(f'{create_url}', json=new_person_data, headers=headers, )
pretty_print(response)

# Getting the ID of the created person instance
if response.status_code == 201:
    created_person = response.json()
    person_id = created_person.get("id")

else:
    print("********************************")
    print("Failed to create a new person")
    exit(1)
# List all persons (GET request)
response = requests.get(base_url)
pretty_print(response)

# Retrieve details of a person (GET request)
# Replace with the actual person's ID you want to retrieve
get_url = f"{detail_url}{person_id}/"
response = requests.get(get_url)
pretty_print(response)

# Update details of an existing person (PUT request)
updated_data = {
    "name": "JPcodes (Updated)",
   
}

response = requests.put(f'{update_url}{person_id}/', json=updated_data, headers=headers)
pretty_print(response)

# Remove a person (DELETE request)
response = requests.delete(f'{delete_url}{person_id}/')
pretty_print(response)
