import streamlit as st
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

# List of all keys
all_keys = [

]


# Streamlit UI
st.title("API Query Streamlit App")

# Get user input for item number
item_no = st.text_input("Enter item number:")

# Create a search box for filtering keys
search_key = st.text_input("Search for a key:")
filtered_keys = [key for key in all_keys if search_key.lower() in key.lower()]

# Create a dropdown for selecting keys
selected_key = st.selectbox("Select a key:", options=filtered_keys, index=0)

# Check if inputs are provided
if st.button("Submit"):
    # Example usage
    response = handle_query(item_no, [selected_key])
    st.write(response)
