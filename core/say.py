import os
from core import ansi


def say(text: str):
	print(text)
	press_any_key_to_continue()

def press_any_key_to_continue():
	import msvcrt
	ch = msvcrt.getch()
