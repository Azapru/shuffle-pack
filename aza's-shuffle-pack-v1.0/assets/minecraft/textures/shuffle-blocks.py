import shutil
import os
import random
import copy

# Create array
blocks = []

for filename in os.listdir("./block-original/"):
    if os.path.isfile(os.path.join("./block-original/", filename)) and not filename.endswith(".mcmeta"):
        blocks.append(filename)

# Randomize
blocksRandom = copy.copy(blocks)
random.shuffle(blocksRandom)

# Clear
if not os.path.isdir("./block/"):
    os.mkdir("./block/")
else:
    shutil.rmtree("./block/")
    os.mkdir("./block/")

# Create
print("==================== Copying blocks... ====================")
i = 0
while (i < len(blocks)):
    print(f"Copying {blocks[i]} as {blocksRandom[i]}")
    shutil.copy("./block-original/"+blocks[i], "./block/"+blocksRandom[i])
    i += 1