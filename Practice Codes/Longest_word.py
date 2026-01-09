def LW():
    sentence = "Artificial intelligence is shaping the future"
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    print(f"Longest word is: {longest_word}")
LW()