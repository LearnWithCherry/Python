# Institution Details Manager!!!
class School:
    def __init__(self, name, Rating, location, streams, hostel, mess, students, lab):
        self.name = name
        self.hostel = hostel
        self.location = location
        self.streams = streams 
        self.Rating = Rating
        self.mess = mess
        self.students = students
        self.lab = lab

    def __str__(self):
        return (f"\n🏫 institution Name: {self.name}\n"
            f"🏢 Hostel: {self.hostel}\n"
            f"📍 Located at {self.location}\n"
            f"⭐ Rated: {self.Rating}\n"
            f"📚 Courses/Streams: {self.streams}\n"
            f"🍇 Mess Available: {self.mess}\n"
            f"👨‍🎓 Students: {self.students}\n"
            f"⚗️ Lab Available: {self.lab}\n")

    def toFileString(self):
        return f"{self.name},{self.hostel},{self.location},{self.Rating},{self.streams},{self.mess},{self.students},{self.lab}\n"

    @staticmethod
    def fromFileString(content):
        parts = content.strip().split(",")
        if len(parts) == 8:
            return School(parts[0],(parts[1]),(parts[2]),int(parts[3]),int(parts[4]),(parts[5]),int(parts[6]),(parts[7]))
        return None

def addName(data_dict):
    institution_map = {"1": "school", "2": "college", "3": "university"}
    institution_input = input("Enter from which Industry are You\n1 = School\n2 = College\n3 = University\nEnter here: ")

    if institution_input not in institution_map:
        print("❌ Invalid Number!!")
        return

    institution = institution_map[institution_input]
    name = input(f"Enter your {institution.title()} name: ")
    Rating = int(bool(input("Enter Rating of you School/collage/University: ")))
    location = input("Enter your School/collage/University location: ")
    streams = int(input("Enter how many streams are there : "))
    hostel = input("Is there a hostel in you School/collage/University(Yes/No): ")
    mess = input("Is mess avalable(Yes/No): ")
    students = int(input("Enter number of students: "))
    lab = input("Is there is an Lab(Yes/No): ")

    data_dict[institution].append(School( name, Rating, location, streams, hostel, mess, students, lab))
    print(f"✅ {institution.title()} added successfully.")

def removeName(data_dict):
    institution = input("From which category do you want to remove?\n(school/college/university): ").lower()
    if institution not in data_dict:
        print("❌ Invalid category!")
        return

    name = input("Enter the name to remove: ")
    for school in data_dict[institution]:
        if school.name.lower() == name.lower():
            data_dict[institution].remove(school)
            print("✅ Removed successfully.")
            return
    print("❌ Not found!")

def viewAll(data_dict):
    institution = input("Which category do you want to view?\n(school/college/university): ").lower()
    if institution not in data_dict:
        print("❌ Invalid category!")
        return

    if not data_dict[institution]:
        print("No entries to display.")
        return

    for school in data_dict[institution]:
        print(school)

def viewOne(data_dict):
    institution = input("From which category do you want to search?\n(school/college/university): ").lower()
    if institution not in data_dict:
        print("❌ Invalid category!")
        return

    name = input("Enter name to search: ")
    for school in data_dict[institution]:
        if school.name.lower() == name.lower():
            print(school)
            return
    print("❌ Not found!")

def saveToFileByType(data_dict):
    for institution, schools in data_dict.items():
        filename = f"18_Projects\\School_data\\{institution}.txt"
        try:
            with open(filename, "w") as f:
                for school in schools:
                    f.write(school.toFileString())
            print(f"💾 Data saved to {filename}")
        except FileNotFoundError:
            print(f"❌ File not found for {institution}")

def loadAllData():
    data_dict = {"school": [], "college": [], "university": []}
    for institution in data_dict.keys():
        filename = f"18_Projects\\School_data\\{institution}.txt"
        try:
            with open(filename, "r") as f:
                for line in f:
                    school = School.fromFileString(line)
                    if school:
                        data_dict[institution].append(school)
        except FileNotFoundError:
            print(f"⚠️ {institution.title()} file not found. Starting with empty data.")
    return data_dict

def menu():
    data_dict = loadAllData()
    while True:
        print("\n--- Welcome to Institution Details ---")
        print("1 = Add New\n2 = Remove\n3 = View All\n4 = View by Search\n5 = Save Data\n6 = Exit")
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                addName(data_dict)
            elif choice == 2:
                removeName(data_dict)
            elif choice == 3:
                viewAll(data_dict)
            elif choice == 4:
                viewOne(data_dict)
            elif choice == 5:
                saveToFileByType(data_dict)
            elif choice == 6:
                print("👋 Thank you! Exiting...")
                break
            else:
                print("⚠️ Invalid choice!")
        except ValueError:
            print("⚠️ Please enter a valid number.")

if __name__ == "__main__":
    menu()
