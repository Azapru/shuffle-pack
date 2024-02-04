import shutil
import os
import random
import copy

# Create array
particles = []

for filename in os.listdir("./particle-original/"):
    if os.path.isfile(os.path.join("./particle-original/", filename)) and not filename.endswith(".mcmeta"):
        particles.append(filename)

# Randomize
particlesRandom = copy.copy(particles)
random.shuffle(particlesRandom)

# Clear
if not os.path.isdir("./particle/"):
    os.mkdir("./particle/")
else:
    shutil.rmtree("./particle/")
    os.mkdir("./particle/")

# Create
print("==================== Copying particles... ====================")
i = 0
while (i < len(particles)):
    print(f"Copying {particles[i]} as {particlesRandom[i]}")
    shutil.copy("./particle-original/"+particles[i], "./particle/"+particlesRandom[i])
    i += 1