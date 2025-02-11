def say(text: str):
    print(text)
    press_any_key_to_continue()


def press_any_key_to_continue():
    from msvcrt import getwch
    ch = getwch()
    if ch == '\x03':
        raise KeyboardInterrupt
