#! python3
"""When this program is running, it replaces the text on the clipboard 
with users chosen chars at the start of each line.
Usage - copying lists of text and adding charts at the beginning of each line

If you have trouble running pyperclip, look at this page
[https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error]
"""

import pyperclip

def add_chars(char):
	text = pyperclip.paste()  # text from clipboard

	lines = text.split('\n') # Separate lines 
	for i in range(len(lines)):
		lines[i] = char + ' ' + lines[i] # add char to each string in 'lines' list
	text = '\n'.join(lines)
	
	pyperclip.copy(text) 


if __name__ == '__main__':
	add_chars('*')
