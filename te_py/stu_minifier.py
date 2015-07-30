import json

students = []

with open("stu.json", 'r') as student_file:
	students = json.load(student_file)

print(json.dumps(students, separators=(',',':')))

