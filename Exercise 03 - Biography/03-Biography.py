info = {
    # Asks the person's name, hometown, and age and waiting for the user's input
    "name": str(input("What is your name?: ")),
    "hometown": str(input("Where are you from?: ")),
}

# Checking if the user's input is an integer
while True:
    int_age = input("How old are you?: ")
    if int_age.isdigit():
        age = int(int_age)
        break
    else:
        print("That's not a valid answer. Please put your age number")

print (info["name"] + "\n" + info["hometown"] + "\n" + int_age)