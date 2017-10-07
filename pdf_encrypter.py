#! python3
""" Encrypter pdf files.
    Walk through directories, copying pdf files, encrypting them.

    Pass password in command line arguments	
"""

import PyPDF2
import sys
import os


def encrypter(password, dir=os.getcwd()):
	for foldername, subfolders, filenames in os.walk(dir):
		for filename in filenames:
			if filename.endswith('.pdf'):
				print('Encrypting ' + filename)
				file = foldername + '/' + filename				
				pdf_file = open(file, 'rb')	
				pdf_reader = PyPDF2.PdfFileReader(pdf_file)

				pdf_writer = PyPDF2.PdfFileWriter()
				for page_num in range(pdf_reader.numPages):
					pdf_writer.addPage(pdf_reader.getPage(page_num))

				pdf_writer.encrypt(password)
				result_pdf = open(file[:-4]+'_encrypted.pdf', 'wb')
				pdf_writer.write(result_pdf)
				result_pdf.close()
				os.remove(file) 
	print("Done. All your pdf files are secure. Don't forget the password")



if __name__ == '__main__':	
	args = sys.argv[1:]

	if not args:
		print('--usage: password')
		sys.exit(1)
	else:
		encrypter(sys.argv[1])
	
