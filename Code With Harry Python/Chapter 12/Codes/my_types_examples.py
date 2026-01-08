
# do not run all these code at the same time!!

########################################################################
n : int = 5

name: str = "Rajat"

def sum(a: int , b: int) -> int:
    return a + b 
result = sum(10 , 20)
print(f"The sum is: {result}")

########################################################################
# problems & solutions 

# Add two numbers!!

def add_numbers(a: int, b: int) -> int:
    return a + b

print("Sum of two numbers is: ",add_numbers(3, 4))  
# Output: 7
########################################################################

# Get first letter:

def first_char(word: str) -> str:
    return word[0]

print("Selected character is: ",first_char("Cherry")) 
# Output: 'C'
########################################################################

# Squared list!

from typing import List

def square_list(nums: List[int]) -> List[int]:
    return [x * x for x in nums]

print(square_list([1, 2, 3])) 
# Output: [1, 4, 9]
########################################################################

#  Q4. Even or Odd Checker

def is_even(n: int) -> bool:
    return n % 2 == 0

print(is_even(4))  # Output: True
########################################################################

#  Q5. Count Vowels

def count_vowels(s: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("Cherry"))  # Output: 2
########################################################################

#  Q6. Average of Marks

from typing import List

def average_marks(marks: List[float]) -> float:
    return sum(marks) / len(marks) if marks else 0.0

print(average_marks([95.5, 88.0, 76.5]))  # Output: 86


