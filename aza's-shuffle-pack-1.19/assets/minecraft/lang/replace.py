import json
import os

# Clear
if os.path.exists("./en_us.json"):
    os.remove("./en_us.json")

# Load JSON
with open("en_us-original.json", "r") as file:
    langJSON = json.load(file)

# Set string
setString = input("Set string (for en_us): ")
for key in langJSON:
    langJSON[key] = setString

# Fix language name
langJSON["language.name"] = "English"
langJSON["language.region"] = "United States"
langJSON["language.code"] = "en_us"

# Save
with open("en_us.json", "w") as file:
    json.dump(langJSON, file, indent=2)