def menu():
    type_menu = {
        "espresso": 150,
        "latte": 200,
        "cappuccino": 250,
        "americano": 180  
    }
    World_Tour_Specials = {
        "turkish coffee": 250,
        "cortado": 200,
        "vienna coffee": 260,
        "cuban espresso": 230,
        "frappuccino": 270
    }
    Sweet_and_Fancy = {
        "caramel latte": 240,
        "hazelnut cappuccino": 260,
        "vanilla cold brew": 230,
        "choco frappe": 250,
        "cookies n cream latte": 280
    }

    print("\n--- 📄 Menu ---")
    choice_num = int(input("1 - Normal coffee\n2 - World special\n3 - Sweet and fancy\nChoose: "))

    if choice_num == 1:
        selected_menu = type_menu
    elif choice_num == 2:
        selected_menu = World_Tour_Specials
    elif choice_num == 3:
        selected_menu = Sweet_and_Fancy
    else:
        print("Sorry..")
        return

    # print the selected menu
    for coffeeName, price in selected_menu.items():
        print(f"{coffeeName.title()} ☕  : ₹{price}")

    order = input("\nSo what do you want to make your day 10x better? ").lower().strip()
    
    if order in selected_menu:
        print(f"\n👉 Price of {order.title()} is ₹{selected_menu[order]} 💰")
        sure = input("Should we make it...").lower()
        if sure == "yes":
            print("-" * 50 + "\n")
            print(f"Sure your {order} will be ready in 2 Minutes⏰\nPlease have a seat..")
        else:
            return menu()
    else:
        print("\n❌ Sorry, we don't have that item 😢")

def Custom():
    def price(cup):
        match cup:
            case "r": return 150
            case "m": return 200
            case "l": return 300
            case "xl": return 350
            case _: return 0   # fallback if wrong input

    def milk(milkType):
        match milkType:
            case "1": return 50   # Normal
            case "2": return 100  # Almond
            case "3": return 100  # Tonned
            case "4": return 10   # Skimmed
            case _: return 0

    def custom(customer):
        match customer:
            case "yes": return 50
            case "no": return 0
            case _: return 0

    print("\n--- 💅 Custom Order Section ---")
    cupSize = input("Cup size (R/M/L/XL): ").lower().strip()
    milkType = input("Milk Type:\n1 = Normal\n2 = Almond\n3 = Tonned\n4 = Skimmed\nChoose: ").lower().strip()
    hotCold = input("How hot/cold you want it: ").lower().strip()
    customer = input("Anything extra (yes/no): ").lower().strip()

    cus = None
    if customer == "yes":
        cus = input("Sure, tell us your vibe: ")
    else:
        print("Alright, keeping it simple 😎")

    print("-" * 30 + "\n")
    mix = (
        f"📝 Order Summary:\n"
        f"- Cup size: {cupSize.upper()} 🥤\n"
        f"- Milk type: {milkType} 🥛\n"
        f"- Temperature: {hotCold} ♨️\n"
        f"- Custom add-on: {cus if cus else 'None'} 💭"
    )
    print(mix)
    
    totalPrice = price(cupSize) + milk(milkType) + custom(customer) + 100
    print(f"\n💰 Total Bill: ₹{totalPrice}\n")

def choice():
    print("--- Welcome to Coffee Addicts Cafe ☕ ---")
    choose = input("Heyy..👋\nDo you want menu📄  or a custom order💅 ?: ").lower().strip()

    if choose == "menu":
        menu()
    elif choose == "custom":
        Custom()
    else:
        print("❓ Please clarify what you want... 🙃")
choice()
