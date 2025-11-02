# NPC-Generator

# 📄 NPC GENERATOR

> *CSAEA final python fundamentals project*


```py
amountofNPC= int(input("How many NPCS do you want to generate(Must be 10+): ")) #USER INPUT ON HOW MANY NPCS TO MAKE
import random

#Possible Attributes for NPCS
Heights=[5.4, 5, 5.7, 6, 6.3,]
Weapons=["Broadsword", "Dagger", "Musket", "Bayyonette", "Bow and Arrow", "Throwing Knife"]
Jobs=["Blacksmith", "Cooper", "Servant","Knight","Soldier", "King"]
Names = ["James", "Jaden", "Brandon", "Logan", "Dexter", "Sylvester", "Edward", "Ashley", "Sarah","Emily","Jamie","Bertha","Ally", "Dorothy"]
#FINAL F STRING TO PRINT ALL THE NPCS
for i in range(amountofNPC):
    print(f"\nName:{random.choice(Names)} \nWeapon: {random.choice(Weapons)} \nJob: {random.choice(Jobs)} \nHeight: {random.choice(Heights)} feet tall \nAge: {random.randint(1,100)}")

This is my NPC Generator for an open world video game being developed by one of my clients. It gives the NPCS Names,Heights, Ages, Jobs, and Weapons and the amount of NPCs is decided by the user. It can create any amount of NPCS you can imagine.


## 🌟 Highlights

Some of the highlights of my generator are that it can take a user input on how many 