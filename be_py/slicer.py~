txt_file = open("raw.txt", 'r')
block = []
student_count = 0

branch = 'branchless ;('
branches = ('ELECTRONICS & TELECOMMU.', 'MECHANICAL', 'COMPUTER', 'INFORMATION TECHNOLOGY')
def print_nice(block):
	for b in block:
		if b.find('MAX.MARKS') != 0:
			print(b)

for line in txt_file:
	line = line.strip()
	if line.find('. . .') == 0:
		if len(block) > 10:
			print("Count " + branch)
			print_nice(block)
			print("End\n")
		else:
			for b in branches:
				for blk in block:
					if not blk.find(b) == -1:
						branch = b
		block = []
	else:
		if line != '':
			block.append(line)

print("EOF")
txt_file.close()

