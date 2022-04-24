import cmd, sys
import getpass

import database

class bcolors:	
	RESET  = '\033[0m'
	GREEN  = '\033[92m'
	YELLOW = '\033[93m'
	RED    = '\033[91m'
	BLUE   = '\033[94m'
	GRAY   = '\033[37m'

good_output = "$[{}Output{}]: ".format(bcolors.GREEN, bcolors.RESET)
warn_output = "$[{}Output{}]: ".format(bcolors.YELLOW, bcolors.RESET)
bad_output = "$[{}OUTPUT{}]: ".format(bcolors.RED, bcolors.RESET)

# ---- Get The Current User's Permissions ---- #
try:
	user = getpass.getuser()
	permission_class = database.get_permissions(user)
except:
	print(bad_output + "You don't seem to have any permissions, seek help.")
	sys.exit()

# ---- Define The User's Shell ---- #
class Shell(cmd.Cmd, permission_class):
	prompt = "$[{}{}{}]: ".format(bcolors.BLUE, user, bcolors.RESET)

	# ---- Close Connection ---- #
	def do_quit(self, arg):
		return True

	# ---- List Commands ---- #
	def do_help(self, arg):
		print("Help!!")
	
	def do_EOF(self, arg):
		pass
	
	def do_print(self, arg):
		print(good_output+arg)

if __name__ == '__main__':
	Shell().cmdloop()
