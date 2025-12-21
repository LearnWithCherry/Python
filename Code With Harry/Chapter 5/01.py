translate = {
    "kaise ho": "how are you",
    "kaha ja rahi ho": "Where are you going",
    "ye mera phone number hai":"This is my phone number"
}

a = input("Enter what you want to transate: ")

print(f"{a} This translate to :- {translate.get(a)}")