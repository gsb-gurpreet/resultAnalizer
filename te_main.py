from subprocess import call

cmd = "pdf2txt.py rawPdfs/te.pdf > raw.txt"
is_pdf2raw_txt = call(cmd, shell=True)
if is_pdf2raw_txt == 0:
	print("Conversion from PDF to Text is Sucessful")

cmd = "python3 te_py/slicer.py > sliced.txt" # < raw.txt
if call(cmd, shell=True) == 0:
	print("slicer")
else:
	print("ABORT ERROR")

cmd = "python3 te_py/jsonizer.py > raw.json" # < sliced.txt
if call(cmd, shell=True) == 0:
	print("jsonizer")
else:
	print("ABORT ERROR")

cmd = "python3 te_py/json_sanitizer.py > sanitized.json" # < raw.json"
if call(cmd, shell=True) == 0:
	print("json_sanitizer")
else:
	print("ABORT ERROR")

cmd = "python3 te_py/subject_jsonizer.py > sub.json" # < sanitized.json"
if call(cmd, shell=True) == 0:
	print("subject_sanitizer")
else:
	print("ABORT ERROR")

cmd = "python3 te_py/student_jsonizer.py > stu.json" # < sanitized.json"
if call(cmd, shell=True) == 0:
	print("student_sanitizer")
else:
	print("ABORT ERROR")


cmd = "python3 te_py/stu_minifier.py > minified_json/te/stu.json" # < stu.json"
if call(cmd, shell=True) == 0:
	print("stu_minifier")
else:
	print("ABORT ERROR")
		

cmd = "python3 te_py/sub_minifier.py > minified_json/te/sub.json" # < sub.json"
if call(cmd, shell=True) == 0:
	print("sub_minifier")
else:
	print("ABORT ERROR")

cmd = "python3 te_py/csv_maker.py > te.csv "#minified_json/se/sub.json" # < sub.json"
if call(cmd, shell=True) == 0:
	print("sub_minifier")
else:
	print("ABORT ERROR")

