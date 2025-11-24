# Creates a dictionary.
names = ["Jake", "Zac", "Sam", "Ron", "Dave", "Ian"]
search = input("Find the person you're looking for in the list: ")
found = False
# Replies if Sam is what the user input or not.
for name in names:
    if name.lower() == search.lower():
        found = True
        if name == "Sam":
            print(f"You found Sam!")
        else:
            print(f"You found {name} but is NOT who you're looking for!")
if not found:
    print("They're not in the list. :(((")