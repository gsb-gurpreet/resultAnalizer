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
		stuPass 	= 0
		stuFail 	= 0
		stuAbsent 	= 0
		midSemList 	= [0] * 31
		endSemList 	= [0] * 71
		totalMrksList 	= [0] * 101
		maxMidSemMrks 	= 0
		minMidSemMrks 	= 30
		avgMidSemMrks 	= -1
		maxEndSemMrks 	= 0
		minEndSemMrks 	= 70
		avgEndSemMrks 	= -1
		maxTotalMrks  	= 0
		minTotalMrks	= 100
		avgTotalMrks	= -1
		midSemMrksSum	= 0
		endSemMrksSum	= 0
		totalMrksSum	= 0
		print(sub.sbKey)
		for st in sub.stus:
#			print(st[2][0], st[2][1])
			if st[2][0].isdigit() and st[2][1].isdigit() and st[2][0] != "AA" and st[2][1] != "AA":
				midSemMrks, endSemMrks = int(st[2][0]), int(st[2][1])
				#result.write(midSemMrks, endSemMrks)
				if ((midSemMrks + endSemMrks) >= 40) and (endSemMrks >= 28):
					stuPass += 1
				else:
					stuFail += 1
				midSemList[midSemMrks] += 1
				endSemList[endSemMrks] += 1
				t = midSemMrks + endSemMrks
				totalMrksList[t] += 1
				if maxMidSemMrks < midSemMrks: maxMidSemMrks = midSemMrks
				if minMidSemMrks > midSemMrks: minMidSemMrks = midSemMrks
				if maxEndSemMrks < endSemMrks: maxEndSemMrks = endSemMrks
				if minEndSemMrks > endSemMrks: minEndSemMrks = endSemMrks
				if maxTotalMrks < t: maxTotalMrks = t
				if minTotalMrks > t: minTotalMrks = t
				midSemMrksSum += midSemMrks
				endSemMrksSum += endSemMrks
				totalMrksSum += t
			else:
				stuAbsent += 1

		stuPsnt = stuPass + stuFail
		# 0 = Reg no., 1 = Name, 2 = mrks
		midSemMerit = []
		for st in sub.stus:
			if st[2][0].isdigit() and st[2][0] != "AA" and st[2][0] != "--":
				midSemMerit.append((st[1], st[2][0]))
		midSemToppers = sorted(midSemMerit, key=lambda t: t[1], reverse=True)
		midSemLoosers = sorted(midSemMerit, key=lambda t: t[1])
		
		endSemMerit = []
		for st in sub.stus:
			if st[2][1].isdigit() and st[2][1] != "AA" and st[2][1] != "--":
				endSemMerit.append((st[1], st[2][1]))
		endSemToppers = sorted(endSemMerit, key=lambda t: t[1], reverse=True)
		endSemLoosers = sorted(endSemMerit, key=lambda t: t[1])
		
		totalMerit = []
		for st in sub.stus:
			if st[2][2].isdigit() and st[2][2] != "AA" and st[2][2] != "--":
				totalMerit.append((st[1], st[2][2]))
		totalToppers = sorted(totalMerit, key=lambda t: t[1], reverse=True)
		totalLoosers = sorted(totalMerit, key=lambda t: t[1])
				
#		for i in range(5):
#			print(totalToppers[i])
		
		webPage = open("page.html", 'w')
		webPage.write("""
<html>
<head>
	<title> %s </title>
	<script type="text/javascript" src="script.js"></script>
</head>
<body>
	<table>
		<tr>
			<td><h1> &nbsp </h1><td>
			<td><img src="../../src/aitlogo2.gif" height="65" width="75" onclick="location.href='../../index.html'"></td>
			<td><h1> &nbsp&nbsp&nbsp </h1><td>
			<td><button onclick="location.href='../home.html'"><b><h2> %s </h2></button></b></td>
			<td><h1> &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp </h1></td>
			<td><h1 align="center"> %s </h1></td>
			<td><h1> &nbsp&nbsp </h1></td>
			<td><button onclick="location.href='excelExport.csv'"> Export to Excel </button></td>
		<tr>
	</table>
	<table>	
	<tr>
		<td>
			<table>
				<tr align="center" colspan="2"><td><b>Student Info	</b></td></tr>
				<tr><td>Total Student</td>		<td>%s</td></tr>
				<tr><td>Students Pass</td>		<td>%s</td></tr>
				<tr><td>Student Fail</td>		<td>%s</td></tr> 
				<tr><td>Student Absent</td>		<td>%s</td></tr>
				<tr><td> &nbsp </td></tr>
				<tr align="center" colspan="2"><td><b>Mid Semester	</b></td></tr>
				<tr><td>Min MidSem Marks</td>		<td>%s</td></tr>
				<tr><td>Max MidSem Marks</td>		<td>%s</td><tr>
				<tr><td>Avg MidSem Marks</td>		<td>%.2f</td><tr>
				<tr><td> &nbsp </td></tr>
				<tr align="center" colspan="2"><td><b>End Semester	</b></td></tr>
				<tr><td>Min EndSem Marks</td>		<td>%s</td><tr>
				<tr><td>Max EndSem Marks</td>		<td>%s</td><tr>
				<tr><td>Avg EndSem Marks</td>		<td>%.2f</td><tr>
				<tr><td> &nbsp </td></tr>
				<tr align="center" colspan="2"><td><b>Total Marks	</b></td></tr>
				<tr><td>Min Total Marks</td>		<td>%s</td><tr>
				<tr><td>Max Total Marks</td>		<td>%s</td><tr>
				<tr><td>Avg Total Marks</td>		<td>%.2f</td><tr>
			</table>
		</td>
		<td>
			<img id="theImage" src="midSem.png" onclick="changeImg()"></img>
		</td>
		<td>
		<div style="height:524px;width:250px;overflow:auto;">
			<table>
				<tr><td align='center'colspan='2'><b> Mid Sem Top 10 </b></td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
			</table>
				<br>
			<table>
				<tr><td align='center'colspan='2'><b> Mid Sem Low 10 </b></td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
			</table>
				<br>
			<table>
				<tr><td align='center'colspan='2'><b> End Sem Top 10 </b></td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
			</table>
				<br>
			<table>
				<tr><td align='center'colspan='2'><b> End Sem Low 10 </b></td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>

			</table>
				<br>
			<table>
				<tr><td align='center'colspan='2'><b> Total Top 10 </b></td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>

			</table>
				<br>
			<table>
				<tr><td align='center'colspan='2'><b> Total Low 5 </b></td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>
				<tr><td> %s </td> <td> %s </td><tr>

			</table>
		</td>
	</tr>
	</table>
</body>
</html>		
		""" % ( (
		 sub.sbBranch + sub.sbKey), sub.sbBranch, sub.sbKey,
		 str(stuPsnt + stuAbsent), str(stuPass), str(stuFail), str(stuAbsent),
		 minMidSemMrks, maxMidSemMrks, midSemMrksSum / stuPsnt,
		 minEndSemMrks, maxEndSemMrks, endSemMrksSum / stuPsnt,
		 minTotalMrks, maxTotalMrks, totalMrksSum / stuPsnt,
		 
		 midSemToppers[0][0], midSemToppers[0][1],
		 midSemToppers[1][0], midSemToppers[1][1],
		 midSemToppers[2][0], midSemToppers[2][1],
		 midSemToppers[3][0], midSemToppers[3][1],
		 midSemToppers[4][0], midSemToppers[4][1],
		 midSemToppers[5][0], midSemToppers[5][1],
		 midSemToppers[6][0], midSemToppers[6][1],
		 midSemToppers[7][0], midSemToppers[7][1],
		 midSemToppers[8][0], midSemToppers[8][1],
		 midSemToppers[9][0], midSemToppers[9][1],

		 midSemLoosers[0][0], midSemLoosers[0][1],
		 midSemLoosers[1][0], midSemLoosers[1][1],
		 midSemLoosers[2][0], midSemLoosers[2][1],
		 midSemLoosers[3][0], midSemLoosers[3][1],
		 midSemLoosers[4][0], midSemLoosers[4][1],
		 midSemLoosers[5][0], midSemLoosers[5][1],
		 midSemLoosers[6][0], midSemLoosers[6][1],
		 midSemLoosers[7][0], midSemLoosers[7][1],
		 midSemLoosers[8][0], midSemLoosers[8][1],
		 midSemLoosers[9][0], midSemLoosers[9][1],
		 
		 endSemToppers[0][0], endSemToppers[0][1],
		 endSemToppers[1][0], endSemToppers[1][1],
		 endSemToppers[2][0], endSemToppers[2][1],
		 endSemToppers[3][0], endSemToppers[3][1],
		 endSemToppers[4][0], endSemToppers[4][1],
		 endSemToppers[5][0], endSemToppers[5][1],
		 endSemToppers[6][0], endSemToppers[6][1],
		 endSemToppers[7][0], endSemToppers[7][1],
		 endSemToppers[8][0], endSemToppers[8][1],
		 endSemToppers[9][0], endSemToppers[9][1],

		 endSemLoosers[0][0], endSemLoosers[0][1],
		 endSemLoosers[1][0], endSemLoosers[1][1],
		 endSemLoosers[2][0], endSemLoosers[2][1],
		 endSemLoosers[3][0], endSemLoosers[3][1],
		 endSemLoosers[4][0], endSemLoosers[4][1],
		 endSemLoosers[5][0], endSemLoosers[5][1],
		 endSemLoosers[6][0], endSemLoosers[6][1],
		 endSemLoosers[7][0], endSemLoosers[7][1],
		 endSemLoosers[8][0], endSemLoosers[8][1],
		 endSemLoosers[9][0], endSemLoosers[9][1],
		 
		 totalToppers[0][0], totalToppers[0][1],
		 totalToppers[1][0], totalToppers[1][1],
		 totalToppers[2][0], totalToppers[2][1],
		 totalToppers[3][0], totalToppers[3][1],
		 totalToppers[4][0], totalToppers[4][1],
		 totalToppers[5][0], totalToppers[5][1],
		 totalToppers[6][0], totalToppers[6][1],
		 totalToppers[7][0], totalToppers[7][1],
		 totalToppers[8][0], totalToppers[8][1],
		 totalToppers[9][0], totalToppers[9][1],

		 totalLoosers[0][0], totalLoosers[0][1],
		 totalLoosers[1][0], totalLoosers[1][1],
		 totalLoosers[2][0], totalLoosers[2][1],
		 totalLoosers[3][0], totalLoosers[3][1],
		 totalLoosers[4][0], totalLoosers[4][1],
		 totalLoosers[5][0], totalLoosers[5][1],
		 totalLoosers[6][0], totalLoosers[6][1],
		 totalLoosers[7][0], totalLoosers[7][1],
		 totalLoosers[8][0], totalLoosers[8][1],
		 totalLoosers[9][0], totalLoosers[9][1],
		 
		 ))
		webPage.close()
		
		scriptFile = open("script.js", 'w')
		scriptFile.write("""
			img_array= new Array("endSem.png", "totalMrks.png", "midSem.png");
			i=0;
			function changeImg(){
				document.getElementById("theImage").src=img_array[i];
				i = (i + 1) % 3;
			}""")
		
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
	out = open( "excelExport.csv", 'w')
	out.write("%s, %s, %s, %s, %s, %s\n" %("ExamId", "StudentName", "MidTerm", "EndTerm", "Total", "Pass"))
	for st in sub.stus:
#		st[0] + ", " + st[1] + ", " + st[2][0] + ", " + st[2][1] + ", " + st[2][2] + ", " + st[3] 	
		out.write("%s, %s, %s, %s, %s, %s\n" %(st[0], st[1], st[2][0], st[2][1], st[2][2], st[3]))
	out.close()


def createDirectoryStructure():
	print("Result Analysis on roll : \n")
	for branch, subs in branchDic.items():
		os.mkdir(branch)
		os.chdir(branch)
		createHome(branch)
		print("###\t", branch, '\n')
		for sub in subs:
			if sub.sbType == "PP":
				print("\t*\t", end = '')
				os.mkdir(sub.sbKey)
				os.chdir(sub.sbKey)
				exportSubCSV(sub)
				calcSub(sub)
				os.chdir("..")
		print("\n")
		os.chdir("..")


def createIndex():
	indexFile = open("index.html", 'w')
	indexFile.write(
	"""
		<html>
			<head>
				<title> Result Analiazer Project </title>
			</head>
			<body>
				<h1 align="center"> Welcome !!! </h1>
				<div align="center">
				<table>
	"""
	)
	for b in branches:
		indexFile.write("""
				<tr><button onclick="location.href='%s/home.html'"><h3>%s</h3></button></tr>
				"""
				% (b, b))

	indexFile.write(
	"""
				</table>
				</div>
			<body>
		</html>
	"""
	)
	indexFile.close()


def createHome(branch):
	indexFile = open("home.html", 'w')
	indexFile.write(
	"""
		<html>
			<head>
				<title> Result Analiazer Project </title>
			</head>
			<body>
				<h1 align="center"> Welcome !!! </h1>
				<div align="center">
				<table>
	"""
	)
	for s in branchDic[branch]:
		if s.sbType == "PP":
			indexFile.write("""
				<tr><button onclick="location.href='%s/page.html'"><h3>%s</h3></button></tr>
				"""
				% (s.sbKey, s.sbKey))

	indexFile.write(
	"""
				</table>
				</div>
			<body>
		</html>
	"""
	)
	indexFile.close()
	

if __name__ == "__main__":
	getInput()
	getSub()
	getStu()
	fillBranches()
	fillSub()
	#calcSub(subList[0])
	createDirectoryStructure()
	createIndex()
