# # using walrus operator 
# if(n := len([1,2,3,4,5,6,7,8,9])) > 5:
#     print(f"List is too long!!\nElements expected less then 5 but it's {n}!!")

# # syntax = variable := expression




# # The Walrus operator is :=, and it was introduced in Python 3.8.
  
# # It allows you to assign a value to a variable as part of an expression.
    
# # This means you can assign and use a value in one line, 
# # which can make your code more concise and sometimes faster.


# # Without Walrus Operator
# value = input("Enter something: ")
# if len(value) > 5:
#     print(f"You entered: {value}")

# # With Walrus Operator
# if (value := input("Enter something: ")) and len(value) > 5:
#     print(f"You entered: {value}")


# The walrus operator lets you assign + use a variable in the same place, 
# especially helpful in loops and conditions.

if (name := input("📝 Enter your name: ")) and len(name) < 5:
    print("❗ Your name is too short! (less than 5 characters)")
else:
    print(f"✅ Hello {name}, you have a nice name!")
