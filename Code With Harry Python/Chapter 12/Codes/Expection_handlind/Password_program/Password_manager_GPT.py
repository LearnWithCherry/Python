def add_password():
    try:
        website = input("🔐 Enter website name: ")
        password = input("🔑 Enter password: ")

        with open("12_Advance_python//Codes//Expection_handlind//Password_program//password.txt", "a") as f:
            f.write(f"{website} : {password}\n")

        print("✅ Password saved successfully!")

    except Exception as e:
        print(f"⚠️ Something went wrong: {e}")


def view_passwords():
    try:
        with open("12_Advance_python//Codes//Expection_handlind//Password_program//password.txt", "r") as f:
            data = f.read()
            if data:
                print("\n📜 Saved Passwords:")
                print(data)
            else:
                print("📭 No passwords saved yet.")

    except FileNotFoundError:
        print("🚫 No password file found. Add one first!")


def main():
    while True:
        print("\n------ PASSWORD MANAGER ------")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Exit")

        try:
            choice = int(input("👉 Enter your choice: "))
            if choice == 1:
                add_password()
            elif choice == 2:
                view_passwords()
            elif choice == 3:
                print("👋 Exiting Password Manager. Bye Cherry!")
                break
            else:
                print("❌ Invalid choice. Enter 1, 2, or 3.")
        except ValueError:
            print("😵 Please enter a valid number!")


# 🚀 Start the program
main()
