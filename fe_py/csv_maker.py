import json

new_students = []

with open("sanitized.json", 'r') as student_file:
	students = json.load(student_file)

headder = "student_name, perma_reg_num, "

for subject in students[0]['subjects']:
	if subject['type'] == "PP":
		headder = headder + subject['code'] + 'oe_marks, '
		headder = headder + subject['code'] + 'th_marks, '
	headder = headder + subject['code'] + 'obtained_marks, '
	headder = headder + subject['code'] + 'is_pass, '
headder = headder + 'total_marks'
print(headder)

for student in students:
	line = ""
	line = line + student['student_name'] + ', '
	line = line + student['perma_reg_num'] + ', '
	
	for subject in student['subjects']:
		if subject['type'] == "PP":
			line = line + str(subject['oe_marks']) + ', '
			line = line + str(subject['th_marks']) + ', '
		line = line + str(subject['obtained_marks']) + ', '
		line = line + str(subject['is_pass']) + ', '

	line = line + str(student['total_marks'])
	print(line)
