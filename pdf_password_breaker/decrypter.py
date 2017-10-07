#! python3
""" Brute-Force PDF Password Breaker
	Say you have an encrypted PDF that you have forgotten the password to, 
	but you remember it was a single English word. Trying to guess your forgotten 
	password is quite a boring task. Instead you can run a program that will decrypt
	the PDF by trying every possible English word until it finds one that works.

	Pass filename that need to crack in command line arguments.
	Important file english_words.txt and encrypted file	should be in a working dir
"""

import PyPDF2
import sys
import os


def decrypter(filename):
	pdf_reader = PyPDF2.PdfFileReader(open(filename, 'rb'))

	english_words = open('english_words.txt')
	list_of_words = english_words.read().split()
	print(len(list_of_words))
	for word in list_of_words:
		if pdf_reader.decrypt(word) == 1:
			print("The password is " + word)
			break



if __name__ == '__main__':	
	args = sys.argv[1:]

	if not args:
		print('--usage: encrypted_filename.pdf')
		sys.exit(1)
	else:
		decrypter(sys.argv[1])
	
