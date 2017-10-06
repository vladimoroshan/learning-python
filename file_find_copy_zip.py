#! python3
""" Program walks through a folder tree and searches for files 
	with a certain file extension (such as .pdf or .jpg). 
	And copy these files from whatever location they are in to a new folder.
	Also makes a zip file of copied files
	
	Usage:  ext - ('str') extension, txt, pdf, jpg, etc
			dir - ('str')the path of a folder from which start search and copying 
			destination - ('str') location or a new name of copied files
"""
import os
import shutil 
import zipfile

current_dir = os.getcwd()

def selective_copy(ext, source=current_dir, destination=current_dir + '/copied'):
	# If you immediately use shutil.copy(), you could get err SameFileError
	files_sourses = [] # copying only after 'walking' in every folder

	if not os.path.exists(destination):
		os.makedirs(destination)
	
	for foldername, subfolders, filenames in os.walk(source):
		#print('The current folder is ' + foldername)
		for subfolder in subfolders:
			#print('SUBFOLDER of ' + foldername + ': ' + subfolder)
			pass

		for filename in filenames:
			#print('FILE INSIDE ' + foldername + ': ' + filename)
			if filename.endswith('.' + ext):				
				# for OS Windows use '\'
				files_sourses.append(foldername+'/'+filename)
				print(filename) 

	for path in files_sourses:
		shutil.copy(path, destination)	

	new_zip = zipfile.ZipFile('copied.zip', 'a')
	paths = os.listdir(destination)		
	for path in paths:
		new_zip.write(destination+'/'+path, compress_type=zipfile.ZIP_DEFLATED)	
	new_zip.close()

if __name__ == "__main__":
	selective_copy('txt')


