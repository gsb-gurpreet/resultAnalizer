from avg import avg
import matplotlib.pyplot as plt

def getList1(subj, test_cases, result):	
	offset = len(subj) - 36
	stuPass = 0
	stuFail = 0
	stuAbs = 0
	totalMidSemMrks = 0
	totalEndSemMrks = 0
	totalMrks = []
	totalMrksList = [0] * 101
	midSemList = [0] * 31
	endSemList = [0] * 71
	test_cases.seek(0)
	for test in test_cases:
		if test.find(subj) == 0:
#			result.write(test[37 + offset : 42 + offset])
			midSemMrks, endSemMrks = test[37 + offset : 42 + offset].split(" ")
			if midSemMrks.isdigit() and midSemMrks.isdigit() and midSemMrks != "AA" and endSemMrks != "AA":
				midSemMrks, endSemMrks = int(midSemMrks), int(endSemMrks)
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
				totalMrks.append(t)
				totalMrksList[t] += 1
			else:
				stuAbs += 1
	
	stuPsnt = stuPass + stuFail
	avgMidSemMrks = totalMidSemMrks / stuPsnt
	avgEndSemMrks = totalEndSemMrks / stuPsnt
	result.write("\nSub : %s\n" % subj)
	result.write("\tTotal Student : %s\n" % str(stuPsnt + stuAbs))
	result.write("\tStudents Pass : %s\n" % str(stuPass))
	result.write("\tStudent Fail  : %s\n" % str(stuFail))
	result.write("\tStudent Absent: %s\n" % str(stuAbs))
	result.write("\tMin Marks     : %s\n" % str(min(totalMrks)))
	result.write("\tMax Marks     : %s\n" % str(max(totalMrks)))
	result.write("\tAverage MidSemMrks : %5.2f\n" % avgMidSemMrks)
	result.write("\tAverage EndSemMrks : %5.2f\n" % avgEndSemMrks)
	result.write("\tAverage Marks      : %5.2f\n" % avg(totalMrks))
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
