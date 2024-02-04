import shutil
import os

# Clear
if os.path.isdir("./block/"):
    shutil.rmtree("./block/")

# Copy
print("==================== Restoring blocks... ====================")
shutil.copytree("./block-original/", "./block/")