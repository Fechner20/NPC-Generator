amountofNPC= int(input("How many NPCS do you want to generate(Must be 10+)?: ")) #USER INPUT ON HOW MANY NPCS TO MAKE
import random

while amountofNPC < 10:
   amountofNPC=int(input("Please enter another number that is 10 or greater: "))

#Possible Attributes for NPCS
Heights=[5.4, 5, 5.7, 6, 6.3,]
Weapons=["Broadsword", "Dagger", "Musket", "Bayonette", "Bow and Arrow", "Throwing Knife"]
Jobs=["Blacksmith", "Cooper", "Servant", "Knight", "Soldier", "King"]
Names = ["James", "Jaden", "Brandon", "Logan", "Dexter", "Sylvester", "Edward", "Ashley", "Sarah", "Emily", "Jamie", "Bertha", "Ally", "Dorothy"]
#FINAL F STRING TO PRINT ALL THE NPCS
for i in range(amountofNPC):
    print(f"\nName:{random.choice(Names)} \nWeapon: {random.choice(Weapons)} \nJob: {random.choice(Jobs)} \nHeight: {random.choice(Heights)} feet \nAge: {random.randint(1,100)}")