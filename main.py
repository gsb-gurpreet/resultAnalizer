import sys

branch = 'branchless ;('
branches = ['ELECTRONICS &TELECOM', 'MECHANICAL', 'COMPUTER', 'INFORMATIOM TECHNOLOGY']
blocks = []
stuList = []
subList = []
branch_dic = {}

class Student:
	def __init__(self, sId, sName, sBranch):
		self.sId = sId
		self.sName = sName
		self.sBranch = sBranch

class Subject:
	def __init__(self, sbKey, sbType, sbBranch):
		self.sbKey = sbKey
		self.sbType = sbType
		self.sbBranch = sbBranch

def getInput():
	test_cases = open(sys.argv[1], 'r')
	temp = []
	# Procuremnet and trival snataitization
	for test in test_cases:
		test = test.strip()
		if test.find('...') == 0:
			if len(temp) > 10:
				temp.append(branch)
				blocks.append(temp)
			temp = []
		else:
			if not test == '':
				temp.append(test)
		for b in branches:
			if not test.find(b) == -1:
				branch = b
	test_cases.close()


def getSub():
	for i in range(len(blocks)):
		for j in range(1, len(blocks[i]) - 3):  # iterating on subject list
			subPsnt = 0 			# 1 subject is present
			subName = blocks[i][j][7:30]
			subMrks = blocks[i][j][27:].split()
			subType = subMrks[0]
			subKey = subName + subType
			subBranch = blocks[i][len(blocks[i]) - 1]
			for sub in subList:
				if sub.sbKey == subKey:
					subPsnt = 1
			if not subPsnt == 1:
				subList.append(Subject(subKey, subType, subBranch))
			
#	for s in subList:		
#		print('subKey =', s.sbKey)


def getStu():
	for i in range(len(blocks)):
		stuId = blocks[i][0][:10].strip()
		stuName = blocks[i][0][13:35].strip()
		totalMrks = 0
		sMrks = []
		for j in range(1, len(blocks[i]) - 3):
			stuBranch = blocks[i][len(blocks[i]) - 1]
			subId = blocks[i][j][:5]
			subName = blocks[i][j][7:30]
			subMrks = blocks[i][j][27:].split()
			subType = subMrks[0]
			subKey = subName + subType
			sub = []
			if subType == 'PP':
				_, _, _, m, e, t, pf = subMrks	#7
				sub.extend([subKey, subType])
				sub.append([m, e, t])
				sub.append(pf)
			elif subType == 'TW' or subType == 'PR' or subType == 'OR':
				_, passMrks, _, twprk, pf = subMrks	#5
				sub.extend([subKey, subType])
				sub.append([twprk, passMrks])
				sub.append(pf)
			else:
				print("NOTHING TO DO HERE")
			sMrks.append(sub)
		stuList.append(Student(stuId, stuName, stuBranch))
		stuList[i].sMrks = sMrks
		sMrks = []
#	print(stuList[0].sId, stuList[0].sName, stuList[0].sBranch, stuList[0].sMrks, sep='\t')
#	for s in stuList:
#		print('name = ', s.sName, 'branch = ', s.sBranch, 'id = ', s.sId)		


def fillBranches():
	temp = []
	for b in branches:
		for s in subList:
			if b == s.sbBranch:
				temp.append(s.sbKey)
		branch_dic[b] = temp
		temp = []
#	print('branch_dic =\n\n')
#	for b in branch_dic:
#		print('branch = ', b)
#		for s in branch_dic[b]:			
#			print(s, '\t')
#		print('\n')


def fillSub():
	# simple printing of mrks obtained by students in his subjects
#	for m in stuList[0].sMrks:
#		print(m,'\n')
	# now printing only the subject key for subjects in student
#	for m in stuList[0].sMrks:
#		print(m[0],'\n')

	students = []
	for sub in subList:
		for stu in stuList:
			if sub.sbBranch == stu.sBranch:
				for sSub in stu.sMrks:
					if sSub[0] == sub.sbKey: # sSub[0] corresponds to subject key on student side
						# DEBUG prints what is to be append in subjects in from of individual student
#						print(stu.sId, stu.sName, sSub[2], sSub[3], sep='\t')						
						students.append([stu.sId, stu.sName, sSub[2], sSub[3]]) # 2 = [m, e, t] OR [twprk, maxMrks] 3 = pf
		sub.stus = students
		students = []
#	print(subList[0].sbKey, subList[0].sbType, subList[0].sbBranch, subList[0].students[0].sName)

def calcSub(sub):
	if sub.sbType == 'PP':
		stuPass = 0
		stuFail = 0
		stuAbsent = 0
		avgMidSemMrks = -1
		avgEndSemMrks = -1
		avgTotalMrks = -1
		midSemList = [0] * 31
		endSemList = [0] * 71
		totalMrksList = [0] * 101
		maxMidSemMrks = 0
		minMidSemMrk0s = 30	
		maxEndSemMrks = 0
		minEndSemMrks = 70
		for st in sub.stus:
			if st[3][0].isdigit() and st[3][1].isdigit() and st[3][0] != "AA" and st[3][1] != "AA":
				midSemMrks, endSemMrks = int(st[3][0]), int(st[3][1])
				#result.write(midSemMrks, endSemMrks)
				if ((midSemMrks + endSemMrks) >= 40) and (endSemMrks >= 28):
					stuPass += 1
				else:
					stuFail += 1
				totalMidSemMrks += midSemMrks
				totalEndSemMrks += endSemMrks
				midSemList[midSemMrks] += 1
				endSemList[endSemMrks] += 1
				t = midSemMrks + endSemMrks
				totalMrksList[t] += 1
			else:
				stuAbsent += 1
		stuPsnt = stuPass + stuFail
		avgMidSemMrks = totalMidSemMrks / stuPsnt
		avgEndSemMrks = totalEndSemMrks / stuPsnt
	#elif sub.sbType == 'OR' or sub.sbType == 'PR' or sub.sbType == 'TW':
	#	stuPass = -1
	#	stuFail = -1
	#	stuAbsent = -1
	#	avgMrks = -1
	#	totalMrksList = [0] * 51
	#	maxMidSemMrks = -1
	#	minMidSemMrks = -1
	#	maxEndSemMrks = -1
	#	minEndSemMrks = -1
		#for s in sub:
	#print("NOTHING TO DO HERE")

def eportSubCSV():
	for sub in subList:
		if sub.sbKey == "COMP. N/W TECHNO.      PP":
			sub.sbKey = "COMP. N-W TECHNO.      PP"
		if sub.sbType == "PP":
			fName = sub.sbKey + ".csv"
			out = open( fName, 'w')
			out.write("%s, %s, %s, %s, %s, %s\n" %("ExamId", "StudentName", "MidTerm", "EndTerm", "Total", "Pass"))
			for st in sub.stus:
				st[0] + ", " + st[1] + ", " + st[2][0] + ", " + st[2][1] + ", " + st[2][2] + ", " + st[3] 	
				out.write("%s, %s, %s, %s, %s, %s\n" %(st[0], st[1], st[2][0], st[2][1], st[2][2], st[3]))
			out.close()

if __name__ == "__main__":
	getInput()
	getSub()
	getStu()
	fillBranches()
	fillSub()
	#calcSub(subList[0])
	eportSubCSV()
