from subprocess import Popen, call
import sys
arg = sys.argv[1]
msg = "go ahead and enjoy it!" if arg == 'y' else "do not touch my food"
call(f"espeak -s125 '{msg}'", shell=True)