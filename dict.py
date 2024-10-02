import json

# Step 2: Read the JSON file
with open('students.json') as f:
    data = json.load(f)

# Step 3: Access the data
students = data['students']

# Step 4: Process the data
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Math Grade: {student['grades']['math']}")
    print(f"Science Grade: {student['grades']['science']}")
    print()
