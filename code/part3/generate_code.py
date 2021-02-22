def Generate(configs_path,image_path):
	print("Generating Program")	
	read_config = open(configs_path, "r", encoding='UTF8')
	write_code = open("detect.py", "w+", encoding='UTF8')

	imports="import numpy as np\nimport cv2\n"
	write_code.write(imports)

	imgline="img = cv2.imread('{}')\n".format(image_path)
	write_code.write(imgline)

	fontt="font = cv2.FONT_HERSHEY_SIMPLEX\n"
	write_code.write(fontt)

	grayy="gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)\n"
	write_code.write(grayy)

	count_lines=0
	def cascade_code(filename,scale_factor,min_neighbours,line):
		write_code.write("cascade = cv2.CascadeClassifier('{}')\n".format(filename))
		write_code.write("objectt = cascade.detectMultiScale(gray,{},{}) \n".format(scale_factor,min_neighbours))
		write_code.write("for (x,y,w,h) in objectt:\n")
		write_code.write("	img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)\n")
		write_code.write("	cv2.putText(img, '{}', (x,y-10), font, 1, (255,255,255), 3)\n".format(line))
	for line in read_config:
		count_lines+=1
		line=line.strip("\n")
		stripped = line.split(" ")
		if len(stripped)==3:
			filename=stripped[0]
			cascade_code(filename,stripped[1],stripped[2],count_lines)
	
	write_code.write("cv2.imshow('img',img)\n")
	write_code.write("cv2.waitKey(0)\n")
	write_code.write("cv2.destroyAllWindows()\n")

	read_config.close()
	write_code.close()
	print("Program Generation Completed")


# configs_path = "F:/pythonSeries/ai series/cascade_classifier/Auto_Cascade_Tester/wow.config"
# image_path = "F:/pythonSeries/ai series/cascade_classifier/gr5.jpg"

# Generate(configs_path,image_path)