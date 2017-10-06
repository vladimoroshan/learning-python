#! python3
""" Downloads file from Internet. Feed up url in command line or copy url 
	and run program. If there are no command line arguments, the program will
	assume the address is stored on the clipboard.
"""

import webbrowser
import requests
import pyperclip
import sys

def download(url='https://www.google.com'):
	#webbrowser.open(url) # just opens url in a new tab

	result = requests.get(url) # downloads the file
	try:
		result.raise_for_status()
	except Exception as exc:
		print('There was a problem: %s' % (exc))

	f = open('downloaded_from_web.txt', 'wb') # create a new file in write binary mode
	for chunk in result.iter_content(100000):
		f.write(chunk)
	f.close()




if __name__ == "__main__":
	if len(sys.argv) > 1:
		# Get address from command line.
		address = ' '.join(sys.argv[1:])
	else:
		# Get address from clipboard.
		address = pyperclip.paste()
	download(address)

