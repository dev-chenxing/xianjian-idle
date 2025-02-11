import time

reset = '\033[0m'
bold = '\033[01m'
underline = '\033[04m'


class fg:
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'
    brightblack = '\033[90m'
    brightred = '\033[91m'
    brightgreen = '\033[92m'
    brightyellow = '\033[93m'
    brightblue = '\033[94m'
    brightmagenta = '\033[95m'
    brightcyan = '\033[96m'
    brightwhite = '\033[97m'


class bg:
    red = '\033[41m'
    green = '\033[42m'
    yellow = '\033[43m'
    blue = '\033[44m'
    magenta = '\033[45m'
    cyan = '\033[46m'
    brightred = '\033[101m'
    brightgreen = '\033[102m'
    brightyellow = '\033[103m'
    brightblue = '\033[104m'
    brightmagenta = '\033[105m'
    brightcyan = '\033[106m'


def color_cat(file: str, slow: bool = False):
    content = reset+color_filter(read_file(file))+reset
    slow_print(content) if slow else print(content, flush=True)


def color_print(content: str, slow: bool = False):
    content = color_filter(reset+content+reset)
    slow_print(content) if slow else print(content, flush=True)


def color_input(content: str):
    return input(fg.blue+content)


def read_file(file: str):
    with open(file, "r", encoding="utf-8") as f:
        return f.read()


def color_filter(content: str):
    if not content:
        return ""

    # Foreground color
    content = content.replace("$black$", fg.black)
    content = content.replace("$red$", fg.red)
    content = content.replace("$green$", fg.green)
    content = content.replace("$yellow$", fg.yellow)
    content = content.replace("$blue$", fg.blue)
    content = content.replace("$magenta$", fg.magenta)
    content = content.replace("$cyan$", fg.cyan)
    content = content.replace("$white$", fg.white)
    content = content.replace("$brightblack$", fg.brightblack)
    content = content.replace("$brightred$", fg.brightred)
    content = content.replace("$brightgreen$", fg.brightgreen)
    content = content.replace("$brightyellow$", fg.brightyellow)
    content = content.replace("$brightblue$", fg.brightblue)
    content = content.replace("$brightmagenta$", fg.brightmagenta)
    content = content.replace("$brightcyan$", fg.brightcyan)
    content = content.replace("$brightwhite$", fg.brightwhite)
    content = content.replace("$normal$", reset)

    # Background color
    content = content.replace("$bgred$", bg.red)
    content = content.replace("$bggreen$", bg.green)
    content = content.replace("$bgyellow$", bg.yellow)
    content = content.replace("$bgblue$", bg.blue)
    content = content.replace("$bgmagenta$", bg.magenta)
    content = content.replace("$bgcyan$", bg.cyan)
    content = content.replace("$HBRED$", bg.brightred)
    content = content.replace("$HBGRN$", bg.brightgreen)
    content = content.replace("$HBYEL$", bg.brightyellow)
    content = content.replace("$HBBLU$", bg.brightblue)
    content = content.replace("$HBMAG$", bg.brightmagenta)
    content = content.replace("$HBCYN$", bg.brightcyan)

    return content


def filter_color(content: str):
    if not content:
        return ""

    # Foreground color
    content = content.replace(fg.black, "")
    content = content.replace(fg.red, "")
    content = content.replace(fg.green, "")
    content = content.replace(fg.yellow, "")
    content = content.replace(fg.blue, "")
    content = content.replace(fg.magenta, "")
    content = content.replace(fg.cyan, "")
    content = content.replace(fg.white, "")
    content = content.replace(fg.brightblack, "")
    content = content.replace(fg.brightred, "")
    content = content.replace(fg.brightgreen, "")
    content = content.replace(fg.brightyellow, "")
    content = content.replace(fg.brightblue, "")
    content = content.replace(fg.brightmagenta, "")
    content = content.replace(fg.brightcyan, "")
    content = content.replace(fg.brightwhite, "")
    content = content.replace(reset, "")

    # Background color
    content = content.replace(bg.red, "")
    content = content.replace(bg.green, "")
    content = content.replace(bg.yellow, "")
    content = content.replace(bg.blue, "")
    content = content.replace(bg.magenta, "")
    content = content.replace(bg.cyan, "")
    content = content.replace(bg.brightred, "")
    content = content.replace(bg.brightgreen, "")
    content = content.replace(bg.brightyellow, "")
    content = content.replace(bg.brightblue, "")
    content = content.replace(bg.brightmagenta, "")
    content = content.replace(bg.brightcyan, "")

    return content


def slow_print(text, pauseAmount=0.05):
    """Slowly print out the characters in text one at a time."""
    for character in text:
        # Set flush=True here so the text is immediately printed:
        print(character, flush=True, end='')  # end='' means no newline.
        time.sleep(pauseAmount)  # Pause in between each character.
    print()  # Print a newline.
