color = input("Enter a color\n(Red/Green/Blue/Orange/Black): ")
match color:
    case "Red" | "red":
        print("You chose Red🔴")
    case "Green" | "green":
        print("You chose Green🟢")
    case "Blue" | "blue":
        print("You chose Blue🔵")
    case  "Orange" | "orange":
        print("You chose Orange🟠")
    case "Black" | "black":
        print("You chose Black⚫")
    case _:
        print("Invalid Choice \nIncorrect Spelling.....!!")