#!/usr/bin/python3

import sys
import os
import matplotlib.pyplot as plt
from avg import avg

branch = 'branchless ;('
branches = ('ELECTRONICS &TELECOM', 'MECHANICAL', 'COMPUTER', 'INFORMATIOM TECHNOLOGY')
blocks = []
stuList = []
subList = []
branchDic = {}

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
		#	Snatize the subject name		
			if subKey == "COMP. N/W TECHNO.      PP":
				subKey = "COMP. N-W TECHNO.      PP"
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
		#	Snatize the subject name		
			if subKey == "COMP. N/W TECHNO.      PP":
				subKey = "COMP. N-W TECHNO.      PP"
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
				temp.append(s)
		branchDic[b] = temp
		temp = []
#	print('branchDic =\n\n')
#	for b in branchDic:
#		print('branch = ', b)
#		for s in branchDic[b]:			
#			print(s.sbKey, '\t')
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
		totalMidSemMrks = 0
		totalEndSemMrks = 0
		midSemList = [0] * 31
		endSemList = [0] * 71
		totalMrksList = [0] * 101
		maxMidSemMrks = 0
		minMidSemMrk0s = 30
		maxEndSemMrks = 0
		minEndSemMrks = 70
		for st in sub.stus:
			print(st[2][0], st[2][1])
			if st[2][0].isdigit() and st[2][1].isdigit() and st[2][0] != "AA" and st[2][1] != "AA":
				midSemMrks, endSemMrks = int(st[2][0]), int(st[2][1])
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
		result = open("summary.txt", 'w')
		result.write("\tTotal Student : %s\n" % str(stuPsnt + stuAbsent))
		result.write("\tStudents Pass : %s\n" % str(stuPass))
		result.write("\tStudent Fail  : %s\n" % str(stuFail))
		result.write("\tStudent Absent: %s\n" % str(stuAbsent))
		result.write("\tMin Marks     : %s\n" % str(min(totalMrksList)))
		result.write("\tMax Marks     : %s\n" % str(max(totalMrksList)))
		result.write("\tAverage MidSemMrks : %5.2f\n" % avgMidSemMrks)
		result.write("\tAverage EndSemMrks : %5.2f\n" % avgEndSemMrks)
		result.write("\tAverage Marks      : %5.2f\n" % avg(totalMrksList))
		result.write("\n\tMidSemList\n")
		for i in range(31):
			result.write("\t%s\t%s\n" %(str(i).rjust(4), str(midSemList[i]).rjust(4)))
		result.write("\n\tEndSemList\n")
		for i in range(71):
			result.write("\t%s\t%s\n" %(str(i).rjust(4), str(endSemList[i]).rjust(4)))
		result.write("\n\ttotalMrksList\n")
		for i in range(101):
			result.write("\t%s\t%s\n" %(str(i).rjust(4), str(totalMrksList[i]).rjust(4)))
		result.write("- . "*30)
		result.close()

		
		plt.bar(range(len(midSemList)), midSemList, align='center', width=.5)
		plt.title('Mid Sem Marks Distrubution')
		plt.xlabel('Marks')
		plt.ylabel('No. of Students')
		plt.savefig('midSem.png')
		plt.close()
		plt.bar(range(len(endSemList)), endSemList, align='center', width=.5)
		plt.title('End Sem Marks Distrubution')
		plt.xlabel('Marks')
		plt.ylabel('No. of Students')
		plt.savefig('endSem.png') 
		plt.close()
		plt.bar(range(len(totalMrksList)), totalMrksList, align='center', width=.5)
		plt.title('Total Marks Distrubution')
		plt.xlabel('Marks')
		plt.ylabel('No. of Students')
		plt.savefig('totalMrks.png') 
		plt.close()

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


def exportSubCSV(sub):
	if sub.sbType == "PP":
		fName = sub.sbKey + ".csv"
		out = open( fName, 'w')
		out.write("%s, %s, %s, %s, %s, %s\n" %("ExamId", "StudentName", "MidTerm", "EndTerm", "Total", "Pass"))
		for st in sub.stus:
			st[0] + ", " + st[1] + ", " + st[2][0] + ", " + st[2][1] + ", " + st[2][2] + ", " + st[3] 	
			out.write("%s, %s, %s, %s, %s, %s\n" %(st[0], st[1], st[2][0], st[2][1], st[2][2], st[3]))
		out.close()


def createDirectoryStructure():
	for branch, subs in branchDic.items():
		os.mkdir(branch)
		os.chdir(branch)
		for sub in subs:
			os.mkdir(sub.sbKey)
			os.chdir(sub.sbKey)
			exportSubCSV(sub)
			calcSub(sub)
			os.chdir("..")
		os.chdir("..")


if __name__ == "__main__":
	getInput()
	getSub()
	getStu()
	fillBranches()
	fillSub()
	#calcSub(subList[0])
	createDirectoryStructure()
