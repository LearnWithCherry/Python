s = {}

spam_comments = {
    "Buy this" , "Click here" , "Won this " , "You got a gift"
}
comments = input("Enter your comment: ")

if(comments in spam_comments):
    print("Its a spam, Do not click!!! ")
else:
    print("Thanks for commenting! ")