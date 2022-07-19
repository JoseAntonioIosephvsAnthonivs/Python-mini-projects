import os 

path = "C:/Users/jojos/Desktop/Atalhos/Python" 

file_count = 0
dir_count = 0

for root, dirs, files in os.walk(path):
	print('Looking in: ', root)
	
	for directories in dirs:
		dir_count += 1
		
	for Files in files:
		file_count += 1
		
print('Number of files: ' , file_count)
print('Number of directories:  ' ,dir_count)
print('Total: ' ,dir_count + file_count)
