resultAnalizer

To run on terminal :

	$ python3 main.py TE.txt


To view the output webSite :

	-	Download this repository from https://github.com/gsb-gurpreet/resultAnalyzer/archive/master.zip

	-	Extract the contents of resultAnalyzer-master.zip	(Extract here)

	-	Open index.html with web browser (It has been tested on Chrome) from resultAnalyser-master folder



For Legacy Code

python3 parser.py <input_PU_result.txt>

here :
	python3 parser.py mit-te-2012.txt

Getting data set :
	Copy from PDF and paste into a txt file and give it as i/p to parser.py
	
Dependencies :
	global:
		matplotlib
		apt-get install python3-matplotlib
	local:
		getList1
		svg.py
	
Exception :
	divideByZero occur if data set doesn't contain any of the written brances
	You'll need to delete the branch folders for running the script again
=======
