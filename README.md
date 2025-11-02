# NPC-Generator

# 📄 NPC GENERATOR

> *CSAEA final python fundamentals project*
This is my NPC Generator for an open world video game being developed for one of my clients. It gives the NPCS Names,Heights, Ages, Jobs, and Weapons and the amount of NPCs is decided by the user. It can create any amount of NPCS you can imagine.


## 🌟 Highlights

Some of the highlights of my generator are that it can take a user input on how many NPCS to create and it only uses one f string to print everything. First, lets talk about the input. I was able to use the input function inside a variable to take in how many NPCS the user wants to make. 
```py
amountofNPC= int(input("How many NPCS do you want to generate(Must be 10+): "))'''
Then we have the one F string that randomizes everything and prints it all out.
'''py 
 print(f"\nName:{random.choice(Names)} \nWeapon: {random.choice(Weapons)} \nJob: {random.choice(Jobs)} \nHeight: {random.choice(Heights)} feet tall \nAge: {random.randint(1,100)}")

