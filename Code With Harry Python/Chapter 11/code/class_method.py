class employee:
    a = 1
    @classmethod
    def show (cls):
        print(f"THe class attribute of a is {cls.a}")

e = employee()
e.a = 45

e.show()

# class method show the attribute value instead of the instance value 
# here class attribute is 1
# instance attribute is 45
# 