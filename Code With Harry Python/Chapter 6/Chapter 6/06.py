# 90 – 100 => Ex 
# 80 – 90 => A 
# 70 – 80 => B 
# 60 – 70  =>C 
# 50 – 60 => D 
# <50  => F 
marks_english = int(input("Enter student marks He She got in English : "))
marks_python = int(input("Enter student marks He She got in Python : "))
marks_data_structure = int(input("Enter student marks He She got in DSA : "))
marks_communication = int(input("Enter student marks He She got in Communication : "))

total_percenate = (marks_english + marks_python + marks_communication + marks_data_structure) / 4

print(total_percenate)
if(total_percenate >= 90 and total_percenate == 100 ) :
    print(f"your Total percenatge is {total_percenate} you got Ex grade")
elif(total_percenate <= 90) :
    print(f"your Total percenatge is {total_percenate} you got A grade")
elif(total_percenate <= 80) :
    print(f"your Total percenatge is {total_percenate} you got B grade")
elif(total_percenate <= 65 and total_percenate == 100 ) :
    print(f"your Total percenatge is {total_percenate} you got C grade")
elif(total_percenate <= 50 ) :
    print(f"your Total percenatge is {total_percenate} you got D grade")
else:
    print("Sorry you couldn't passed the exam!! ")