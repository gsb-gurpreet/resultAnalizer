from subprocess import call

cmd = "pdf2txt.py rawPdfs/be.pdf > raw.txt"
is_pdf2raw_txt = call(cmd, shell=True)
if is_pdf2raw_txt == 0:
	print("Conversion from PDF to Text is Sucessful")

cmd = "python3 be_py/slicer.py > sliced_temp.txt" # < raw.txt
if call(cmd, shell=True) == 0:
	print("slicer")
else:
	print("ABORT ERROR")

cmd = "python3 be_py/back_blocker.py > sliced.txt" # < sliced_temp.txt
if call(cmd, shell=True) == 0:
	print("back_bloker")
else:
	print("ABORT ERROR")

cmd = "python3 be_py/jsonizer.py > raw.json" # < sliced.txt
if call(cmd, shell=True) == 0:
	print("jsonizer")
else:
	print("ABORT ERROR")

cmd = "python3 be_py/json_sanitizer.py > sanitized.json" # < raw.json"
if call(cmd, shell=True) == 0:
	print("json_sanitizer")
else:
	print("ABORT ERROR")

cmd = "python3 be_py/subject_jsonizer.py > sub.json" # < sanitized.json"
if call(cmd, shell=True) == 0:
	print("subject_sanitizer")
else:
	print("ABORT ERROR")

cmd = "python3 be_py/student_jsonizer.py > stu.json" # < sanitized.json"
if call(cmd, shell=True) == 0:
	print("student_sanitizer")
else:
	print("ABORT ERROR")


cmd = "python3 be_py/stu_minifier.py > minified_json/be/stu.json" # < stu.json"
if call(cmd, shell=True) == 0:
	print("stu_minifier")
else:
	print("ABORT ERROR")
		

cmd = "python3 be_py/sub_minifier.py > minified_json/be/sub.json" # < sub.json"
if call(cmd, shell=True) == 0:
	print("sub_minifier")
else:
	print("ABORT ERROR")


cmd = "python3 be_py/csv_maker.py > be.csv "#minified_json/se/sub.json" # < sub.json"
if call(cmd, shell=True) == 0:
	print("sub_minifier")
else:
	print("ABORT ERROR")

