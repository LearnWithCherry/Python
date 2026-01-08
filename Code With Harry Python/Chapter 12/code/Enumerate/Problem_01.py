students = ["Ankit", "Riya", "Tina", "Rohit", "Sourav", "Cherry"]

passed_count = 0
failed_count = 0
passed_students = []
failed_students = []

print("🎓 Exam Results\n---------------------------")

for index, student in enumerate(students, start=1):
    if index % 2 == 0:
        print(f"Roll No: {index} - {student} ✅ Passed")
        passed_count += 1
        passed_students.append(student)
    else:
        print(f"Roll No: {index} - {student} ❌ Failed")
        failed_count += 1
        failed_students.append(student)

# Summary Section
print("\n📊 Summary Report")
print("---------------------------")
print(f"✅ Total Passed Students: {passed_count}")
print(f"❌ Total Failed Students: {failed_count}")

print("\n🏅 Passed Students:")
for name in passed_students:
    print(f"👉 {name}")

print("\n📕 Failed Students:")
for name in failed_students:
    print(f"❌ {name}")
