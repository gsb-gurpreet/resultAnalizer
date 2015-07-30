def adjust_capital(name):
	name = name.split()
	words = []
	for nam in name:
		nam = nam.lower()
		first_letter, *rest = nam
		first_letter = first_letter.upper()
		words.append(first_letter + join(rest, sep=""))
	return join(words)
			 
def join(in_str, sep=" "):
	joined_str = ""
	for i in in_str:
		joined_str = joined_str + sep + i
	return joined_str.strip()

def process_footer(footer):
	#print(str(footer))
	_, footer = footer.split('=')
	footer = footer.strip()
	footer, _ = footer.split('/')
	footer = footer.strip()
	print('"total_marks":"' + footer + '",')

def process_subjects(subjects):
	print("[")
	for subject in subjects:
		leading, trailling = subject[:37], subject[37:]
		leading, trailling = leading.strip(), trailling.strip()
		subject_code, *subject_name = leading.split('.')
		subject_name = adjust_capital(join(subject_name))
		print('{')
		print('"code":"' + subject_code + '",')
		print('"name":"' + subject_name + '",')

		trailling = trailling.split()
		print('"type":"' + trailling[0] + '",')
		print('"max_marks":"' + trailling[1] + '",')
		#print('"pass_marks":"' + trailling[2] + '",')
		if len(trailling) == 5:
			print('"obtained_marks":"' + trailling[3] + '",')
			print('"is_pass":"' + trailling[4] + '"')
		elif len(trailling) == 7:
			print('"oe_marks":"' + trailling[3] + '",')
			print('"th_marks":"' + trailling[4] + '",')
			print('"obtained_marks":"' + trailling[5] + '",')
			print('"is_pass":"' + trailling[6] + '"')
		else:
			print("ERROR CRROUPT I/P")		
		if subject != subjects[len(subjects) - 1]: 
			print('},')
		else:
			print('}')
	print("]")

def process_header(header):
	seat_num = ""
	student_name = ""
	mom_name = ""
	for i in range(len(header)):
		header[i] = header[i].strip()
		header[i] = header[i].split(',')
		#print("header[" + str(i) + "] = " + str(header[i]))
	header[0] = join(header[0])
	seat_num, *_ = header[0].split()
	student_name, mom_name = header[0][11:36], header[0][37:]
	student_name = adjust_capital(student_name)
	mom_name = adjust_capital(mom_name)
	#print('"seat_num":"' + seat_num + '",')
	print('"student_name":"' + student_name + '",')
	print('"mom_name":"' + mom_name + '",')
	perma_reg_num = header[1][0]
	#college 	  = header[2][0]
	#prev_seat_num = header[3][0]
	print('"perma_reg_num":"' + perma_reg_num + '",')
	#print('"prev_seat_num":"' + prev_seat_num + '",')


txt_file = open("sliced.txt", 'r')

lines = []
subjects = []

for i in txt_file:
	lines.append(i)
txt_file.close()

print('[')

for i in range(len(lines)):
	if lines[i].find("Count") == 0:
		header = lines[i + 1].strip().split(',')
		k = i
		while not lines[k].find("End") == 0:
			k = k + 1
		offset = k - i - 1
		for j in range(2, offset):
			subjects.append(lines[i + j].strip())
		footer = lines[i + offset]
		print('{')
		process_header(header)
		process_footer(footer)
		branch = lines[i][6:].strip()
		branch = adjust_capital(branch)
		print('"branch": "' + branch + '",')
		print('"subjects":')
		process_subjects(subjects)
		if i < (len(lines) - 20):
			print('},')
		else:
			print('}')
		subjects = []
		
print(']')

