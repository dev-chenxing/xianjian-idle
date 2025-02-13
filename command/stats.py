from core.ansi import color_print as print
from core.common import MAX_NUMBER

pattern = "状态"

def callback():
	from core.common import game
	李逍遥 = game.李逍遥
	print(f"$brightyellow${李逍遥.name}\n")
	print(f"经验值  $yellow${李逍遥.经验值}$normal$ / $blue${calc_exp_required(李逍遥.修行)}")
	print(f"修行    $yellow${李逍遥.修行}")
	print(f"体力  $yellow${李逍遥.当前体力}$normal$ / $blue${李逍遥.体力}")
	print(f"真气  $yellow${李逍遥.当前真气}$normal$ / $blue${李逍遥.真气}")
	print(f"武术   $yellow${李逍遥.武术}")
	print(f"灵力   $yellow${李逍遥.灵力}")
	print(f"防御   $yellow${李逍遥.防御}")
	print(f"身法   $yellow${李逍遥.身法}")
	print(f"吉运   $yellow${李逍遥.吉运}")



def calc_exp_required(current_level: int):
	exp_required = int(15 + current_level*(current_level-1)*25/2)
	return exp_required if exp_required < MAX_NUMBER else 32000
