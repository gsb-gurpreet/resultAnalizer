txt_file = open("raw.txt", 'r')
block = []
student_count = 0

def print_nice(block):
	for b in block:
		print(b)

for line in txt_file:
	line = line.strip()
	if line.find('...') == 0:
		if len(block) > 10:
			student_count = student_count + 1
			print("Count = " + str(student_count))
			print_nice(block) 
			print("End\n")
		block = []
	else:
		if not line == '':
			block.append(line)

print("EOF")
txt_file.close()
