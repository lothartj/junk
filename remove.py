import json
import pandas as pd

# Your provided JSON data
data = {

}

# Remove values from all keys
for key in data:
    data[key] = None

# Convert the modified data to a pandas DataFrame
df = pd.json_normalize(data)

# Save to an Excel file
excel_filename = "output_data.xlsx"
df.to_excel(excel_filename, index=False)


print(f"Data has been saved to {excel_filename}")