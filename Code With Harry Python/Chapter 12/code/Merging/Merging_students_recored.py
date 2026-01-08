branch_a = {
    'Alice': 85,
    'Bob': 78,
    'Charlie': 90
}

branch_b = {
    'Bob': 82,       # duplicate student, updated grade
    'Diana': 88,
    'Eve': 91
}

# ✅ Merge them using the pipe operator
merged_records = branch_a | branch_b

# 🔍 Show the final record
print("📋 Final Student Grades (Merged):")
for student, marks in merged_records.items():
    print(f"{student}: {marks}")

