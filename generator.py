mannames = ["James", "Jaden", "Brandon", "Logan", "Dexter", "Sylvester", "Edward"]
femalenames = ["Ashley", "Sarah","Emily","Jamie","Bertha","Ally", "Dorothy"]
amountofNPC= input("How many NPCS do you want to generate(Must be 10+): ")
import random

#Possible Attributes for NPCS
Heights=["5'4", "6'6", "5'7", "6'", "5'10"]
Weapons=["Broadsword", "Dagger", "Musket", "Bayyonette", "Bow and Arrow", "Throwing Knife"]
Gender=["Male", "Female"]
Age = random.int(1,100)


gender=random.choice(Gender)

# GENERATOR

for a in range(amountofNPC):
 if gender == "Female":
    print(f"Name: {random.choice(femalenames)}")
else:
    print(f"Name: {random.choice(mannames)}")
print(f"Height: {random.choice(Heights)}")
print(f"Weapon: {random.choice(Weapons)}")
print(f"Gender: {random.choice(Gender)}")
print(f"Age: {(Age)}")




   
    





