#! python3
""" Program walks through a folder tree and searches for files 
	with a certain file extension (such as .pdf or .jpg).

	Usage:  source - ('str')the path of a folder from which start search 
						and deleting
			max_size - ('int') in Mb. Files greater size than max_size will be
					    deleted.
			ext - ('str') extension, txt, pdf, jpg, etc
""" 
import os

current_dir = os.getcwd()

def del_files(source=current_dir, max_size=100, ext=''):
	
	for foldername, subfolders, filenames in os.walk(source):
		#print('The current folder is ' + foldername)
		
		for filename in filenames:
			#print('DELETING_FILE ' + foldername + ': ' + filename)
			file = foldername+'/'+filename
			size = os.path.getsize(file)			
			if size > (max_size*1000*1024) and filename.endswith(ext): 
				print(filename, size)
				#os.remove(file) # Uncomment this line to delete files. Careful!


if __name__ == "__main__":
	del_files(current_dir, 100, 'mp4')

