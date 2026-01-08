from datetime import datetime

while True:
    print("\n========= Simple Menu =========")
    print("1. Greet Me")
    print("2. Show Current Date & Time")
    print("3. Exit")
    
    choice = input("Enter your choice (1/2/3): ")

    match choice:
        case "1":
            name = input("Enter your name: ")
            print(f"Hello, {name}! 😊")
        
        case "2":
            now = datetime.now()
            print("📅 Current date and time:", now.strftime("%Y-%m-%d %H:%M:%S"))

        case "3":
            print("👋 Exiting... Bye Cherry!")
            break

        case _:
            print("⚠️ Invalid choice. Please try again.")
