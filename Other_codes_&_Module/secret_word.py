secret_word = "Artificial intelligence"
guess = ""
guess_limit = 5
guess_count = 0

print("---------------HINTS-----------------------------")
print("It's so popular nowadays!")
print("Used to make videos without any camera or team.")
print("Needs prompts to use it!!")
print("--------------Guess the word-----------------------------")

while guess_count < guess_limit:
    guess = input(f"Guess {guess_count + 1}/{guess_limit}: ")
    guess_count += 1
    
    if guess.lower() == secret_word.lower():
        print("--------------Guessed It Right-----------------------------")
        print(f"🎉 You guessed it in {guess_count} tries! The word is: {secret_word}")
        break
    else:
        print("❌ Wrong guess. Try again.")

if guess.lower() != secret_word.lower():
    print("--------------Sorry-----------------------------")
    print(f"😔 You didn't guess the word in {guess_limit} tries. The correct word was: {secret_word}")
