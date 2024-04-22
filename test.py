import streamlit as st
from transformers import pipeline
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

# Set up a question-answering pipeline
qa_pipeline = pipeline("question-answering", model="bert-base-uncased", tokenizer="bert-base-uncased")

# Streamlit UI
st.title("API Query Streamlit App with Question-Answering")

# Get user input in a chat format
user_input = st.text_input("You:", key="user_input")

# Check if user has provided input
if user_input:
    # Example usage with GPT-3
    response = handle_query(user_input, ["Description"])
    
    # Display bot's response in a chat format
    st.text("Bot:")
    st.write(response)

    # Use the question-answering pipeline to generate a response
    api_key = "extracted_key_from_user_input"  # Implement logic to extract a key from the user's input
    data = get_data(api_key)
    answer = qa_pipeline(question=user_input, context=data)

    # Display the question-answering response
    st.text("Question-Answering Bot:")
    st.text(answer['answer'])
