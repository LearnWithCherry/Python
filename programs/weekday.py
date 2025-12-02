class Solution:
    def whichWeekDay(self, day):
        days = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        print(days.get(day, "Invalid"))
    
a = (input("Enter a Number: "))
s = Solution()
s.whichWeekDay(a)