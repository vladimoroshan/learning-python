#! python3
""" Finds email addresses from the clipboard. Print it and save in the file 
Press CTRL-A to select all the text on the page, and press CTRL-C to copy it 
to the clipboard. When you run this program, this output email addresses
"""
import pyperclip
import re
import os

email_regex = re.compile(r'''(
			[a-zA-Z0-9._%+-]+      # username
			@                      # at symbol
			[a-zA-Z0-9.-]+         # domain name
			(\.[a-zA-Z]{2,4})      # dot-something
	       )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in email_regex.findall(text):
	matches.append(groups[0]) 

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard: ')
	print('\n'.join(matches))
	
	# create a file to story results, rewrite it if it is already exists	
	f = open(os.path.abspath('.') + '/email_adresses.txt', 'w')
	f.write('\n'.join(matches))
	f.close()

else:
	print("No email addresses found")
