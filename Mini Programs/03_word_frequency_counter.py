def Most_words():
    with open("15_Daily_Questions\\words.txt", 'r') as file:
        text = file.read().lower()
    
    words = text.split()  # split into list of words
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    # Sort dictionary by frequency, descending
    sorted_words = sorted(freq.items(), key=lambda item: item[1], reverse=True)

    print("Top 5 most frequent words:")
    for word, count in sorted_words[:5]:
        print(f"{word}: {count}")

# Correct function call
Most_words()
