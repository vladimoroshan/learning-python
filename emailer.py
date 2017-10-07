#! python3
""" Command Line Emailer

    Program that takes an email address and string of text on the command line 
    and then, using Selenium, logs into your email account and sends an email of 
    the string to the provided address. 

    For this program, you’ll need the Firefox web browser. If you don’t already
    have Firefox, you can download it for free from http://getfirefox.com/.

    Also you need to specify your email address and password in the corresponding
    variables at the top of function, after you can run program from terminal.

    ATTENTIOM: when I wrote this script gmail had ids and classes names as specified.
    But it can change. If script not running inspect gmail pages. 	
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import time



def emailer(address, text):
	url = 'https://mail.google.com/mail'
	email = 'vlad.moroshan@gmail.com'
	password = 'Lemon2016'

	browser = webdriver.Firefox() 
	browser.get(url) 

	email_elem = browser.find_element_by_id('identifierId')
	print(email_elem)
	email_elem.send_keys(email)

	next_elem = browser.find_element_by_id('identifierNext')
	next_elem.click()

	time.sleep(10)

	password_elem = browser.find_elements_by_class_name('whsOnd zHQkBf"')
	password_elem.send_keys(password)

	submit_elem = browser.find_element_by_id('passwordNext')
	submit_elem.click()

	time.sleep(10)

	write_btn = browser.find_element_by_class_name('T-I J-J5-Ji T-I-KE L3')
	write_btn.click()

	time.sleep(10)

	to = browser.find_element_by_id('dk')
	to.send_keys(address)

	to = browser.find_element_by_id(':d0')
	to.send_keys(text)

	submit = browser.find_element_by_class_name('T-I J-J5-Ji aoO T-I-atl L3')
	submit.click()
	
	print('Your mail was sent')


def main():
	args = sys.argv[1:]

	if not args:
		print('--usage: email address, message')
		sys.exit(1)
	else:
		emailer(args[0], args[1])


if __name__ == '__main__':
	main()
