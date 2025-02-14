from wcwidth import wcswidth
from .ansi import color_input as input, filter_color, filter_color_ansi
import core.logging as log

def string_width(text: str):
	return wcswidth(filter_color(text))


def input_to(callback: callable, *arg):
	log.debug("input_to("+callback.__name__+")")
	response = input('> ')
	callback(filter_color(response))

def ljust(text, length, padding = " "):
	return text + padding * max(0, (length - string_width(text)))

def rjust(text, length, padding = " "):
	return padding * max(0, (length - string_width(text))) + text

def justify(left, right, length, padding=" "):
	return left + padding * max(0, length - (string_width(left)+string_width(right))) + right
