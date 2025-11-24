def oddoreven(n):
    # Detects if its odd or even
    if n % 2 == 0:
        print(f"Even")
    else:
        print(f"Odd")
# Asks for the number
def main():
        number = int(input("Give any number: "))
        oddoreven(number)
main()