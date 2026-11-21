import json
txt_data = "Heyyy! I'm testing files!"
filepath = r"C:\Users\Hoor Arafa\OneDrive\Desktop\Plan\Day 6\names.json"
employee = {
    "name": "Donkey",
    "age": 10,
    "gender" : "idiot"
}
try:
    with open(filepath,"r") as file:
        # file.write(txt_data)
        names = json.load(file)
        print(f"json file '{filepath}' was read!")
except FileExistsError:
    print("FILE EXISTS IDIOT")

print(names)   
print(type(names)) 

file2 = r"C:\Users\Hoor Arafa\OneDrive\Desktop\Plan\Day 6\person.json"

try:
    with open(file2,"r") as file2:
        people = json.load(file2)
        print("PERSON (HOOR) READ!")
except FileExistsError:
    print("EXISTS")  

print(people)
print(type(people))          