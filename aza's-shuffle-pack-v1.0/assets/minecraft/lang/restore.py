import os
import shutil

print("==================== Restoring strings... ====================")

# Clear
if os.path.exists("./en_us.json"):
    os.remove("./en_us.json")

# Restore
shutil.copy("./en_us-original.json", "./en_us.json")