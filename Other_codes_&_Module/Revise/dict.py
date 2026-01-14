marks = {
    "Rajat" : 60,
    "Ansh" : 50,
    "Ruhi" : 70
#    keys  : items
}

# empty_dict = {}
# print(type(marks))
# print(marks["Rajat"])

# methods

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"Ruhi":80})
# print(marks)


print(marks.get("Rajat")) # if key does not exist then return none

# sets will only print value single time even if the value repeats
# ----------------------------------------------------------------

# s = {1,2,3,4,5,5,5,6,6,7,7,7,7,8}
# empty_set = set()  this is how u can make an empty set
# print(s)

# sets methods

# s.add(10)

# print(len(s)) # length of the value 
# s.remove(10) # remove selected value

# print(s)

s1 = {1,2,3,4}
s2 = {4,5,6,7}

# print(s1.union(s2)) # does not print repeated values = {1, 2, 3, 4, 5, 6, 7}
# print(s1.intersection(s2)) # print only repeated values = {4}


# Problems

translate = {
    "How are you" : "Kaise hai aap",
    "What are you doing" : "aap kya kr rahe ho",
    "How was your day" : "Aap din kaisa tha"
    # key             item
} 
# word = input("Enter: ")
# print(translate[word])
# s = set()
# total = int(input("Enter: "))
# i=1
# while(i<total+1):
#     number = int(input(f"Enter {i} Number: "))
#     s.add(number)
#     i = i+1

# print(s)

p1 = "hello"

comm = input("Comment: ").lower()

if p1 in comm:
    print("Scam")
else:
    print("Thanks")