import sys
from core.ansi import color_print as print

pattern = "^退出游戏"


def callback():
	print("$red$✖$normal$ 退出游戏")
	sys.exit()
