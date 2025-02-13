from core.ansi import color_print as print

DEBUG = True

def debug(text: str):
	if DEBUG:
		print("[DEBUG] "+text)

def error(text: str):
	print("$red$[ERROR] "+text)
