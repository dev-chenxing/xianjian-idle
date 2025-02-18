import importlib
import os
import pathlib
import re
import core.logging as log

command_dir = "command"
cmd_patterns = {}
log.debug("Scanning command directory for cmd files...")
for file in os.listdir(command_dir):
	path = pathlib.Path(os.path.join(command_dir,file))
	if path.is_file():
		name = path.stem
		cmd = importlib.import_module(command_dir+"."+name)
		if hasattr(cmd, "pattern") and hasattr(cmd, "callback"):
			log.debug("Found cmd file $yellow$"+name+" "+cmd.pattern)
			cmd_patterns[cmd.pattern] = cmd.callback
		else:
			log.error(f"Found invalid cmd file {name}")

def parse_cmds(param: str):
	for pattern, cmd in cmd_patterns.items():
		matches = re.match(pattern, param)
		# log.debug("Matching pattern "+pattern+" with command "+param)
		if matches:
			log.debug("Matched command pattern $green$"+pattern+"$normal$")
			if len(matches.groups()) > 0:
				args = matches[1]
				cmd(args)
			else:
				cmd()
