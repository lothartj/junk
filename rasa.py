import requests

# API URL and authentication details
api_url = ""
username = ""
password = ""

# Function to make API requests
def make_api_request(query):
    # Formulate the complete URL
    full_url = f"{api_url}?{query}"
    
    # Make the API request with basic authentication
    response = requests.get(full_url, auth=(username, password))
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

# Function to handle user queries
def handle_query(item_no, target_keys):
    # Construct the select part of the query
    select_query = ",".join(target_keys)
    
    query = f"$filter=No eq '{item_no}'&$select={select_query}"
    result = make_api_request(query)

    # Check if any items were found in the response
    if result.get("value"):
        item_data = result["value"][0]
        response = {key: item_data.get(key, f"Key '{key}' not found") for key in target_keys}
        return response
    else:
        return f"Error: No items found for item No '{item_no}'"

# Get user input for item number
item_no = input("Enter item number: ")

# Get user input for keys (comma-separated)
keys_input = input("Enter keys (comma-separated): ")
target_keys = [key.strip() for key in keys_input.split(",")]

# Example usage
response = handle_query(item_no, target_keys)
print(response)
