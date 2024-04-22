import requests
import pandas as pd

# API URL
api_url = ""

# Your credentials
username = ""
password = ""

# Make a request to the API with authentication
response = requests.get(api_url, auth=(username, password))

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON
    data = response.json()

    # Extract relevant information
    items = data.get("value", [])
    extracted_data = [{"No": item.get("No", ""),"Description":item.get("Description",""), "Net_Weight": item.get("Net_Weight", ""), "Gross_Weight": item.get("Gross_Weight", "")} for item in items]

    # Create a DataFrame from the extracted data
    df = pd.DataFrame(extracted_data)

    # Write the DataFrame to an Excel file
    excel_file = "output.xlsx"
    df.to_excel(excel_file, index=False)

    print(f"Data has been successfully written to {excel_file}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(response.text)
