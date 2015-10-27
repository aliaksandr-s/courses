import os

def rename_files():
	#get filenames
	file_list = os.listdir(r'C:\Users\Aliaksandr\Desktop\courses\Udacity\Programming Foundations with Python\prank')
	print file_list

	#delete digits from name
	os.chdir(r'C:\Users\Aliaksandr\Desktop\courses\Udacity\Programming Foundations with Python\prank')
	for x in file_list:
		os.rename(x, x.translate(None, '1234567890'))

rename_files()