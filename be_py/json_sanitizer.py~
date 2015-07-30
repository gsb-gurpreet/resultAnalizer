import json

with open("raw.json", 'r') as student_file:
	students = json.load(student_file)
	
for student in students:
	for subject in student['subjects']:
		subject['max_marks'] = int(subject['max_marks'])
		#subject['pass_marks'] = int(subject['pass_marks'])
		if subject['is_pass'] == "P":
			subject['is_pass'] = True
		else:
			subject['is_pass'] = False

		if subject['obtained_marks'].isdigit():
			subject['obtained_marks'] = int(subject['obtained_marks'])
		else:
			subject['obtained_marks'] = 0
		
for student in students:
	if student["total_marks"].isdigit():
		student["total_marks"] = int(student["total_marks"])
	else:
		total_marks = 0
		for subject in student['subjects']:
			total_marks = total_marks + subject['obtained_marks']
		student["total_marks"] = total_marks

for student in students:
	for subject in student['subjects']:
		subject['code'] = subject['code'] + ' ' + subject['type']

print(json.dumps(students, sort_keys = True, indent = 4, separators=(', ',': ')))
