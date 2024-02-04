import subprocess
import os

blocks = input("Shuffle blocks?     (Y - yes | N - no, do not change | D - restore default): ").upper()
items = input("Shuffle items?      (Y - yes | N - no, do not change | D - restore default): ").upper()
particles = input("Shuffle particles?  (Y - yes | N - no, do not change | D - restore default): ").upper()
text = input("Shuffle text?       (Y - yes | N - no, do not change | D - restore default | R - replace all strings): ").upper()

# Text
os.chdir("./assets/minecraft/lang/") # Change working directory to lang
if text == "Y":
    subprocess.run(["python", "./shuffle.py"], check=True)
elif text == "N":
    pass
elif text == "D":
    subprocess.run(["python", "./restore.py"], check=True)
elif text == "R":
    subprocess.run(["python", "./replace.py"], check=True)
else:
    print(f"Incorrect command: text={text}")
os.chdir(os.path.dirname(os.path.abspath(__file__))) # Restore working directory

# Change working directory to textures
os.chdir("./assets/minecraft/textures/")

# Blocks
if blocks == "Y":
    subprocess.run(["python", "./shuffle-blocks.py"], check=True)
elif blocks == "N":
    pass
elif blocks == "D":
    subprocess.run(["python", "./restore-blocks.py"], check=True)
else:
    print(f"Incorrect command: blocks={blocks}")

# Items
if items == "Y":
    subprocess.run(["python", "./shuffle-items.py"], check=True)
elif items == "N":
    pass
elif items == "D":
    subprocess.run(["python", "./restore-items.py"], check=True)
else:
    print(f"Incorrect command: items={items}")

# Particles
if particles == "Y":
    subprocess.run(["python", "./shuffle-particles.py"], check=True)
elif particles == "N":
    pass
elif particles == "D":
    subprocess.run(["python", "./restore-particles.py"], check=True)
else:
    print(f"Incorrect command: particles={particles}")

input("Finished! (Press ENTER to exit)")
