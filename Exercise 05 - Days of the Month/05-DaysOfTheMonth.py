# Store the months in dictionary
months = {
    1: ("January", 31),
    2: ("February", 28), 
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}
# Asks for the user's input
month = int(input("Put any month number: "))
if month < 1 or month > 12:
    print("That is not a number in the months! Please put any number from 1 to 12")
else:
    month_name, days = months[month]
    # If the user puts in february
    if month == 2:
        leap_year = input("Leap year? Type YES or NO if it is or not.")
        if leap_year.lower() == "yes":
            days = 29
    print(f"The {month_name} have {days} days.")