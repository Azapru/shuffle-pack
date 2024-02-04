import json
import random
import os

print("==================== Randomizing strings... ====================")

# Clear
if os.path.exists("./en_us.json"):
    os.remove("./en_us.json")

# Load JSON
with open("en_us-original.json", "r") as file:
    langJSON = json.load(file)

valuesList = list(langJSON.values())

# Shuffle
random.shuffle(valuesList)

# Update JSON
langJSON.update(zip(langJSON.keys(), valuesList))

# Fix language name
langJSON["language.name"] = "English"
langJSON["language.region"] = "United States"
langJSON["language.code"] = "en_us"

# Save
with open("en_us.json", "w") as file:
    json.dump(langJSON, file, indent=2)