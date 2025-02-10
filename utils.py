from ansi import color_input as input, filter_color


def input_to(callback: callable, *arg):
    response = input('> ')
    callback(filter_color(response))
