import shutil
import os
import random
import copy

# Create array
items = []

for filename in os.listdir("./item-original/"):
    if os.path.isfile(os.path.join("./item-original/", filename)) and not filename.endswith(".mcmeta"):
        items.append(filename)

# Randomize
itemsRandom = copy.copy(items)
random.shuffle(itemsRandom)

# Clear
if not os.path.isdir("./item/"):
    os.mkdir("./item/")
else:
    shutil.rmtree("./item/")
    os.mkdir("./item/")

# Create
print("==================== Copying items... ====================")
i = 0
while (i < len(items)):
    print(f"Copying {items[i]} as {itemsRandom[i]}")
    shutil.copy("./item-original/"+items[i], "./item/"+itemsRandom[i])
    i += 1