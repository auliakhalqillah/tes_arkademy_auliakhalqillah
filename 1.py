import json
# Input by user
name = str(input("Name\t\t\t\t:"))
age = int(input("Age\t\t\t\t:"))
address = str(input("Address\t\t\t\t:"))
n_hobbies = int(input("How many hobbies do you have\t:"))

hobbies = []
for i in range(n_hobbies):
    hoby = str(input("Hobbies\t\t\t\t:"))
    hobbies.append(hoby)
is_married = bool(input("Do you married? [Y/N]\t\t:"))
if (is_married == "Y" or is_married == "y"):
    married = "YES"
else:
    married = "NO"

school = str(input("School\t\t\t\t:"))
yearin = int(input("Start\t\t\t\t:"))
yearout = int(input("End\t\t\t\t:"))
major = str(input("Major\t\t\t\t:"))
list_school = {
    "school": school,
    "year_in": yearin,
    "year_out": yearout,
    "major": major,
}

skills = []
nskill = int(input("How many skill do you have\t:"))
print("[Skill level: Beginer,Advance,Expert]")
for j in range(nskill):
    skill = {
        str(input("Skill\t\t\t\t:")):str(input("level\t\t\t\t:"))
    }
    skills.append(skill)

interest_in_coding = str(input("Do you interest in coding? [Y/N]:"))
if (interest_in_coding == "Y" or interest_in_coding == "y"):
    interest = "YES"
else:
    interest = "NO"

# Store to the dict
data = {
  "name": name,
  "age": age,
  "address": address,
  "hobbies": hobbies,
  "married": married,
  "list_school": list_school,
  "skills": skills,
  "interest in coding": interest,
}

# Convert to the json file
with open('1.json', 'w') as outfile:
    json.dump(data, outfile)
print("\nResult has been saved in JSON file")
