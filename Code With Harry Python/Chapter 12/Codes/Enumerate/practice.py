# Used to loop over a list and keep track of the index + value.
print("problem - 1")
fruit = ["Apple" , "Mango" , "Cherry" , "guava" ]
for index , value in enumerate(fruit , start=1):
    print(index , value)

print(" ")
# output
'''
0 Apple
1 Mango
2 Cherry
3 guava

'''
# start = 1 lets you decide from which number you want to start the list 
'''
1 Apple
2 Mango
3 Cherry
4 guava
'''
# Track Index While Looping
print("problem - 2")
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"{index}: {color}")

print(" ")
print("problem - 3")
#  Start Index from a Specific Number
for i, color in enumerate(colors, start=1):
    print(f"Color {i}: {color}")

print(" ")
# Use with if Conditions
print("problem - 4")
names = ["Cherry", "GPT", "Lazy", "Learner"]
for i, name in enumerate(names , start=1):
    if "Lazy" in name:
        print(f"'Lazy' found at index {i}")

print(" ")
# printing words with even index only
print("problem - 5")
words = ["Python", "is", "super", "fun"]

for index, word in enumerate(words):
    if index % 2 == 0:  # Even index check
        print(f"Index {index}: {word}")


print(" ")
# printing words with odd index only
print("problem - 6")
words = ["Python", "is", "super", "fun"]

for index, word in enumerate(words):
    if index % 2 != 0:  # odd index check
        print(f"Index {index}: {word}")

