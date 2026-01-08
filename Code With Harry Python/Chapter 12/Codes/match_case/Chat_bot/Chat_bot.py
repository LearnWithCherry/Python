# chat bot 
import random
import time
def bot():
    print("Hello User!!")
    while True:
        user = input("\nAsk for list to know What i can do\nAsk Me: ").strip().lower()

        match user:
            case "list":
                print("------------------List-------------------------------")
                with open("12_Advance_python//Codes//match_case//Chat_bot//list.txt") as f:
                    print(f.read())
            case "hi":
                print("-------------------------------------------")
                print("Hello\nNice to meet you👋")
            case "how are you":
                print("-------------------------------------------")
                print("Thanks For Asking I am Good☺️")
            case "what are you doing":
                print("-------------------------------------------")
                print("Nothing Just Interacting With Users🤝")
            case "what time it is":
                print("-------------------------------------------")
                print("The Current time is ⌛", time.ctime())
            case "tell me a story":
                print("-------------------------------------------")
                try:
                    with open("12_Advance_python//Codes//match_case//Chat_bot//story.txt") as f:
                        print(f.read())
                except FileNotFoundError:
                    print("📁 Oops! Couldn't find the story file.")
            case "tell me a random number":
                print("-------------------------------------------")
                print("🔢 Generating Random Number: ",random.randint(1,100))
            case "exit":
                print("-------------------------------------------")
                print("Exiting Bot📤\nBye....Bye....👋")
            case _:
                print("Sorry😓\nI am learning new thing please Enter Something Else!")
            
bot()


# ✅ How to Fix the UnicodeDecodeError
# When opening a file, just tell Python to use UTF-8, which supports all characters:
# with open(r"12_Advance_python\Codes\match_case\story.txt", encoding="utf-8") as f:
#     print(f.read())
# write this code if there are different types of characters