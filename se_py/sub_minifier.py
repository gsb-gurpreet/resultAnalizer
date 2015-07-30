import json

subjects = []

with open("sub.json", 'r') as subject_file:
	subjects = json.load(subject_file)

print(json.dumps(subjects, separators=(',',':')))

