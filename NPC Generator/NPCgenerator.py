#A program to generate a random name and traits for dnd NPCs


#A LOT OF IMPORTS
import os
import time
import random


#function to generate an human name
def human_extract():
   
    print("Extracting Data...")
    time.sleep(1)
    
    with open(files["humanfirst"], "r") as humanfirst_file, open(files["humanlast"], "r") as humanlast_file:
    
        firstlines = [line.strip() for line in humanfirst_file]
        lastlines = [line.strip() for line in humanlast_file]
    #if text is detected. will randomly select a line from the txt file and return it as the name
    if firstlines and lastlines:
        generated_firstname = random.choice(firstlines)
        generated_lastname = random.choice(lastlines)
        return generated_firstname, generated_lastname
    else: #If it doesnt detect text it will return error msg
        return "No human names found"
    
#Function to generate an elven name
def elven_extract():
   
    print("Extracting Data...")
    time.sleep(1)
    
    with open(files["elvenfirst"], "r") as elffirst_file, open(files["elvenlast"], "r") as elflast_file:
    
        firstlines = [line.strip() for line in elffirst_file]
        lastlines = [line.strip() for line in elflast_file]
    #if text is detected. will randomly select a line from the txt file and return it as the name
    if firstlines and lastlines:
        generated_firstname = random.choice(firstlines)
        generated_lastname = random.choice(lastlines)
        return generated_firstname, generated_lastname
    else: #If it doesnt detect text it will return error msg
        return "No elven names found"

#function to generate a dwarven name
def dwarven_extract():
   
    print("Extracting Data...")
    time.sleep(1)
    
    with open(files["dwarvenfirst"], "r", encoding="utf-8") as dwarvenfirst_file, open(files["dwarvenlast"], "r", encoding="utf-8") as dwarvenlast_file:
    
        firstlines = [line.strip() for line in dwarvenfirst_file]
        lastlines = [line.strip() for line in dwarvenlast_file]
    #if text is detected. will randomly select a line from the txt file and return it as the name
    if firstlines and lastlines:
        generated_firstname = random.choice(firstlines)
        generated_lastname1 = random.choice(lastlines)#the lastname txt file gets pulled from twice to generate a unique last name
        generated_lastname2 = random.choice(lastlines).lower()

        #loop to make sure the 2 last names arent the same
        while generated_lastname1 == generated_lastname2:
            generated_lastname2 = random.choice(lastlines)


        generated_lastname = generated_lastname1+ generated_lastname2
        return generated_firstname, generated_lastname
    else: #If it doesnt detect text it will return error msg
        return "No dwarven names found"
    
#function to generate a tiefling name
def tiefling_extract():
   
    print("Extracting Data...")
    time.sleep(1)
    
    with open(files["tieflingfirst"], "r") as tieflingfirst_file, open(files["tieflinglast"], "r") as tieflinglast_file:
    
        firstlines = [line.strip() for line in tieflingfirst_file]
        lastlines = [line.strip() for line in tieflinglast_file]
    #if text is detected. will randomly select a line from the txt file and return it as the name
    if firstlines and lastlines:
        generated_firstname = random.choice(firstlines)
        generated_lastname = random.choice(lastlines)
        return generated_firstname, generated_lastname

    else: #If it doesnt detect text it will return error msg
        return "No tiefling names found"


#Generate random traits
def traits():
    #Determine what traits the user wants
    print("\nGenerating Traits...")
    time.sleep(1)

    with open(files["positive_traits"], "r") as ptraits_file, open(files["negative_traits"], "r") as ntraits_file:
  
        ptrait_lines = [line.strip() for line in ptraits_file]
        ntrait_lines = [line.strip() for line in ntraits_file]

        if ptrait_lines and ntrait_lines:
            ntrait = random.choice(ntrait_lines)
            ptrait = random.choice(ptrait_lines)
            return ntrait, ptrait
        else:
            return "No traits found"
        
def negotiation():
    #Determine negotiation motivation/pitfalls
    with open(files["neg"], "r") as neg_file:

        lines = [line.strip() for line in neg_file]

        if lines:
            motivation = random.choice(lines)
            pitfall = random.choice(lines)
            return motivation, pitfall
        else:
            return "No negotiation table found"




#Set working directory
base_path = r"C:\Users\Drew\Desktop\NPC Generator"

files = {
    "elvenfirst": os.path.join(base_path, "elvenfirst.txt"),
    "elvenlast": os.path.join(base_path, "elvenlast.txt"),
    "humanfirst": os.path.join(base_path, "humanfirst.txt"),
    "humanlast": os.path.join(base_path, "humanlast.txt"),
    "dwarvenfirst": os.path.join(base_path, "dwarvenfirst.txt"),
    "dwarvenlast": os.path.join(base_path, "dwarvenlast.txt"),
    "tieflingfirst": os.path.join(base_path, "tieflingfirst.txt"),
    "tieflinglast": os.path.join(base_path, "tieflinglast.txt"),
    "positive_traits": os.path.join(base_path, "positive_traits.txt"),
    "negative_traits": os.path.join(base_path, "negative_traits.txt"),
    "neg": os.path.join(base_path, "negotiation.txt"),

}


#Main Code

#Ask what kind of npc they want generated. (Update to a GUI in future)


#Get user input
print("Please select the race for the NPC\n")
try:
    race = int(input("""1: Human 
2: Elf 
3: Dwarf 
4: Tiefling
Input: """))
except:
    print("Invalid input. Select a valid number for selection.")

#If statement to generate name based on selection
if race == 1:
    firstname,lastname = human_extract()
elif race == 2:
    firstname,lastname = elven_extract()
elif race ==3:
    firstname,lastname = dwarven_extract()
elif race ==4:
    generated_name = tiefling_extract()



#Generate Traits
ntrait,ptrait = traits()
#generate negotiation style
motivation,pitfall = negotiation()

#Final print statement of generated NPC

print(f"\nName: {firstname} {lastname}")
print(f"\nTraits\nPositive: {ptrait}, Negative: {ntrait}")
print(f"\nNegotiation\nMotivation: {motivation}, Pitfall: {pitfall}")

time.sleep(10)#add loop and ability to manually end the program

