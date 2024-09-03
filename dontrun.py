import pygetwindow as gw
import random

def add(a, b):
	if b == 0:
		return a
	else:
		return add (a+1 , b-1)
shake = 10
wall = gw.getAllWindows()
while True:
	for w in wall:
		if w._getWindowRect().right > 0:
			w.move(random.randrange(-2,3),random.randrange(-2,3))
			w.resize(random.randrange(-shake,shake+1),random.randrange(-shake,shake+1))