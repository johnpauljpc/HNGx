import requests, json

# Define the base URL of your Django API
base_url = "http://localhost:8000/api/"  # Replace with your API's URL

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
    "name": "JP codes"
}
response = requests.post(base_url, json=new_person_data, headers=headers, )
pretty_print(response)

# Getting the ID of the created person instance
if response.status_code == 201:
    created_person = response.json()
    user_id = created_person.get("id")

else:
    print("********************************")
    print("Failed to create a new person")
    exit(1)

    
# List all persons (GET request)
response = requests.get(base_url)
pretty_print(response)

# Retrieve details of a person (GET request)
get_user_url = f"{base_url}{user_id}/"
response = requests.get(get_user_url)
pretty_print(response)

# Update details of an existing person (PUT request)
updated_data = {
    "name": "JPcodes (Updated)",
   
}

response = requests.put(get_user_url, json=updated_data, headers=headers)
pretty_print(response)

# Remove a person (DELETE request)
response = requests.delete(get_user_url)
pretty_print(response)
