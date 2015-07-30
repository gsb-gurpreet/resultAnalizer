txt_file = open("sliced_temp.txt", 'r')

lines = []

for i in txt_file:
	lines.append(i)
txt_file.close()

for i in range(len(lines)):
	if lines[i].find("Count") == 0:
		branch = lines[i][6:].strip()
		if branch == "INFORMATIOM TECHNOLOGY":
			offset = -1
		else:
			offset = 0
		if len(str(lines[i + 5])) < 60:
			for j in range(i, i + 16 + offset):
				print(lines[j], end='')

txt_file.close()
