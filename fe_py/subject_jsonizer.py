import json
from pprint import pprint
subjects = []

def is_subject_present(subj):
	for sub in subjects:
		if sub['code'] == subj:
			return True
	return False

with open("sanitized.json", 'r') as student_file:
	students = json.load(student_file)

# for adding basic subject info
for student in students:
	for subject in student['subjects']:
		if not is_subject_present(subject['code']):
			new_sub = {}
			new_sub['code'] = subject['code']
			new_sub['max_marks'] = subject['max_marks']
			new_sub['name'] = subject['name']
			new_sub['type'] = subject['type']
			subjects.append(new_sub)

for l_sub in subjects:
	if l_sub['type'] == "PP":
		obtained_marks_list = [0] * (l_sub['max_marks'] + 1)
		oe_marks_list = [0] * 51
		th_marks_list = [0] * 51
		pass_count = 0
		fail_count = 0
		for student in students:
			for subject in student['subjects']:
				if l_sub['code'] == subject['code']:
					obtained_marks_list[subject['obtained_marks']] = obtained_marks_list[subject['obtained_marks']] + 1
					oe_marks_list[subject['oe_marks']] = oe_marks_list[subject['oe_marks']] + 1
					th_marks_list[subject['th_marks']] = th_marks_list[subject['th_marks']] + 1
					if subject['is_pass']:
						pass_count = pass_count + 1
					else:
						fail_count = fail_count + 1
					l_sub['obtained_marks_list'] = obtained_marks_list
					l_sub['oe_marks_list'] = oe_marks_list
					l_sub['th_marks_list'] = th_marks_list
					l_sub['pass_count'] = pass_count
					l_sub['fail_count'] = fail_count
					
	elif l_sub['type'] == "PR" or l_sub['type'] == "TW":
		obtained_marks_list = [0] * (l_sub['max_marks'] + 1)
		pass_count = 0
		fail_count = 0
		for student in students:
			for subject in student['subjects']:
				if l_sub['code'] == subject['code']:
					obtained_marks_list[subject['obtained_marks']] = obtained_marks_list[subject['obtained_marks']] + 1
					if subject['is_pass']:
						pass_count = pass_count + 1
					else:
						fail_count = fail_count + 1
					l_sub['obtained_marks_list'] = obtained_marks_list
					l_sub['pass_count'] = pass_count
					l_sub['fail_count'] = fail_count
	else:
		print("HELL broke loose")
		
print(json.dumps(subjects, sort_keys = True, indent = 4, separators=(', ',': ')))
