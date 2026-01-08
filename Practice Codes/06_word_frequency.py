def word_Freq_check():
    # Sample paragraph
    text = "Python is GreAt. Python is ,easy to learn! Learn .Python programming."
    
    # Step 1: Remove punctuation
    for char in [",",".","!","'","/"]:
        text = text.replace(char," ")
    # Step 2: Convert to lowercase
    text = text.lower()
    
    # Step 3: Split into words
    words = text.split()
    
    # Step 4: Count word frequencies
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    # Step 5: Sort by frequency (highest first), then alphabetically
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    # Step 6: Print results
    for word, count in sorted_freq:
        print(f"{word}: {count}")
# Run the function
word_Freq_check()
