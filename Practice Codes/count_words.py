def count():
    filename = "18_Projects\\01_Small_projects\\TXT_files\\words.txt"
    try:
        with open(filename, "r") as file:
            content = file.read()
            print("-----🖨️  Printing Content-----")
            
            words = content.split()
            total_words = len(words)
            if total_words == 0:
                print("----- File is Empty -----")
                return
            elif total_words <= 10:
                print(content)
            else:
                # take first 3 words and last 3 words
                first_half = " ".join(words[:7])
                last_half = " ".join(words[-5:])
                print(f"{first_half} ---------------------------------  {last_half}")
            
            print(f"There are in total {total_words} Words...")
            full_content = input("Want to see the full content press Enter: ").lower()
            if full_content == "":
                print("------🖨️  Printing Full Content------")
                print(content)
                print("--- Thank you ---")
            else:
                print("Thank you...👋👋")
    
    except FileNotFoundError:
        print("File Not Found")

count()
