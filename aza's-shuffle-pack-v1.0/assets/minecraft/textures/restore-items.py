import shutil
import os

# Clear
if os.path.isdir("./item/"):
    shutil.rmtree("./item/")

# Copy
print("==================== Restoring items... ====================")
shutil.copytree("./item-original/", "./item/")