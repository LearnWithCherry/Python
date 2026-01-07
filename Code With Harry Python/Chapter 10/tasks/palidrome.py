def palidrome():
    user = input("Enter a Palidrome String: ")
    cleaned = "".join(ch.lower() for ch in user if ch.isalnum())
    print(cleaned)
palidrome()

