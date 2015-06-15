#!/usr/bin/env python3

import sys
import os
import matplotlib
from getList1 import getList1 as gl1

test_cases = open(sys.argv[1], 'r')
	
branches = {"entc" : ["304181 DIGI. COMMUNICATION PP 100 40", "304182 DIGITAL SIGNAL PRO. PP 100 40", "304183 MICRO CONTR. & APPL. PP 100 40", "304184 ELECTROM & TRANS LI PP 100 40", "304185 SYS. PROG. & OP SYS PP 100 40"], "comp" : ["310241 THEORY OF COMPU. PP 100 40", "310242 OPERATING SYS DESIGN PP 100 40", "310243 D COM & WIRE SEN NW PP 100 40", "310244 DATA MGMT & SYS. APP PP 100 40", "310245 COMP FORE & CYB APP PP 100 40"], "it" : ["314441 COMP. N/W TECHNO. PP 100 40", "314442 THEO OF COMPUTA. PP 100 40", "314443 DBMS PP 100 40", "314444 SOFTWARE ENGINEERING PP 100 40","314445 WEB ENGI AND TECHNO PP 100 40"]} 
#"meh" : ["302041 DES. OF MACH ELE – I PP 100 40","302042 HEAT TRANSFER PP 100 40","302043 THEORY OF MACH-II PP 100 40","302044 METRO & QTY CTRL PP 100 40","302045 HYDRA & PNEU PP 100 40"]}

for branch, subs in branches.items():
	os.mkdir(branch)
	os.chdir(branch)
	for sub in subs:
		os.mkdir(sub[:7])
		os.chdir(sub[:7])
		result = open("result.txt", 'w')
		gl1(sub, test_cases, result)
		os.chdir("..")
		result.close()
	os.chdir("..")
#	print("-" * 80)

test_cases.close()
