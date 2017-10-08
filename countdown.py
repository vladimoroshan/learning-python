#! python3
# A very basic countdown script 

import time
import sys
import webbrowser

def countdown(seconds):
	timeleft = seconds
	print('Countdown started') 
	while timeleft > 0:
		print(timeleft, end='\n')
		time.sleep(1)
		timeleft = timeleft - 1

	webbrowser.open('https://www.youtube.com/watch?v=QZSMSxODaLo', new=2)
	print('Time is over')



if __name__ == '__main__':	
	args = sys.argv[1:]

	if not args:
		print('--usage: countdown.py int(time in seconds)')
		sys.exit(1)
	else:
		countdown(int(sys.argv[1]))
