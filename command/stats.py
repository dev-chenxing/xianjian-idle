from core.ansi import color_print as print
from core.common import MAX_NUMBER
import core.logging as log
from core.utils import justify, string_width

pattern = "状态"

def callback():
	from core.common import game
	李逍遥 = game.李逍遥
	print(f"$brightyellow${李逍遥.name}\n")
	stats = {
		"经验值": 李逍遥.经验值, 
		"修行": 李逍遥.修行, 
		"体力": 李逍遥.体力, 
		"真气": 李逍遥.真气, 
		"武术": 李逍遥.武术, 
		"灵力": 李逍遥.灵力, 
		"防御": 李逍遥.防御, 
		"身法": 李逍遥.身法, 
		"吉运": 李逍遥.吉运
		}
	max_len = max([string_width(stat_name+str(stat)) for stat_name, stat in stats.items()])
	print(f"{justify(left="经验值", right=f"$yellow${李逍遥.经验值}", length=max_len+2)}$normal$ / $blue${calc_exp_required(李逍遥.修行)}")
	print(justify(left="修行", right=f"$yellow${李逍遥.修行}", length=max_len+2))
	print(f"{justify(left="体力", right=f"$yellow${李逍遥.当前体力}", length=max_len+2)}$normal$ / $blue${李逍遥.体力}")
	print(f"{justify(left="真气", right=f"$yellow${李逍遥.当前真气}", length=max_len+2)}$normal$ / $blue${李逍遥.真气}")
	print(justify(left="武术", right=f"$yellow${李逍遥.武术}", length=max_len+2))
	print(justify(left="灵力", right=f"$yellow${李逍遥.灵力}", length=max_len+2))
	print(justify(left="防御", right=f"$yellow${李逍遥.防御}", length=max_len+2))
	print(justify(left="身法", right=f"$yellow${李逍遥.身法}", length=max_len+2))
	print(justify(left="吉运", right=f"$yellow${李逍遥.吉运}", length=max_len+2))



def calc_exp_required(current_level: int):
	exp_required = int(15 + current_level*(current_level-1)*25/2)
	return exp_required if exp_required < MAX_NUMBER else 32000
