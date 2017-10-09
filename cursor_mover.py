import pyautogui

pyautogui.PAUSE = 10
pyautogui.FAILSAFE = True

width, height = pyautogui.size()
print(width, height)

pos = pyautogui.position()
print(pos)

print('Press CTRL-C to stop mouse cursor from nudging')

while True:
	pyautogui.moveRel(1, 1)
	pyautogui.moveRel(-1, -1)
