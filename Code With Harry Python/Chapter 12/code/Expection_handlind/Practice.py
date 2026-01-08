def div():
    try:
        num = int(input("Enter the first number: "))
        num1 = int(input("Enter the second number: "))
        result = num / num1
        print(f"✅ Result: {result}")
    except ZeroDivisionError:
        print("❌ You cannot divide by zero!")
    except ValueError:
        print("❌ Please enter only numbers.")
    finally:
        print("📌 Operation Completed.")

div()
