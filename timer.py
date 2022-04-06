# Quickly start the timer inside the terminal

import time
import terminal

def countdown(t):
	while t:
		mins, secs = divmod(t, 60)
		timer = '{:02d}:{:02d}'.format(mins, secs)
		print(terminal.blue(timer), end="\r")
		time.sleep(1)
		t -= 1
	
	print(terminal.colorize('That\'s it!', '#FFBF00'))

t = input("Enter the time in seconds: ")

countdown(int(t))
