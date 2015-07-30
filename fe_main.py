from subprocess import call

cmd = "pdf2txt.py rawPdfs/fe.pdf > raw.txt"
is_pdf2raw_txt = call(cmd, shell=True)
if is_pdf2raw_txt == 0:
	print("Conversion from PDF to Text is Sucessful")

cmd = "python3 fe_py/slicer.py > sliced.txt" # < raw.txt
if call(cmd, shell=True) == 0:
	print("slicer")
else:
	print("ABORT ERROR")

cmd = "python3 fe_py/jsonizer.py > raw.json" # < sliced.txt
if call(cmd, shell=True) == 0:
	print("jsonizer")
else:
	print("ABORT ERROR")

cmd = "python3 fe_py/json_sanitizer.py > sanitized.json" # < raw.json"
if call(cmd, shell=True) == 0:
	print("json_sanitizer")
else:
	print("ABORT ERROR")

cmd = "python3 fe_py/subject_jsonizer.py > sub.json" # < sanitized.json"
if call(cmd, shell=True) == 0:
	print("subject_sanitizer")
else:
	print("ABORT ERROR")

cmd = "python3 fe_py/student_jsonizer.py > stu.json" # < sanitized.json"
if call(cmd, shell=True) == 0:
	print("student_sanitizer")
else:
	print("ABORT ERROR")


cmd = "python3 fe_py/stu_minifier.py > minified_json/fe/stu1.json" # < stu.json"
if call(cmd, shell=True) == 0:
	print("stu_minifier")
else:
	print("ABORT ERROR")
		

cmd = "python3 fe_py/sub_minifier.py > minified_json/fe/sub1.json" # < sub.json"
if call(cmd, shell=True) == 0:
	print("sub_minifier")
else:
	print("ABORT ERROR")

cmd = "python3 fe_py/csv_maker.py > fe.csv "#minified_json/fe/sub.json" # < sub.json"
if call(cmd, shell=True) == 0:
	print("sub_minifier")
else:
	print("ABORT ERROR")

