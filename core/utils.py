from .ansi import color_input as input, filter_color
import core.logging as log


def input_to(callback: callable, *arg):
	log.debug("input_to("+callback.__name__+")")
	response = input('> ')
	callback(filter_color(response))
