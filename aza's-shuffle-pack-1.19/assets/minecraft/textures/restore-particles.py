import shutil
import os

# Clear
if os.path.isdir("./particle/"):
    shutil.rmtree("./particle/")

# Copy
print("==================== Restoring particles... ====================")
shutil.copytree("./particle-original/", "./particle/")