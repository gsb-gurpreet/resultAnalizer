
			img_array= new Array("endSem.png", "totalMrks.png", "midSem.png");
			i=0;
			function changeImg(){
				document.getElementById("theImage").src=img_array[i];
				i = (i + 1) % 3;
			}