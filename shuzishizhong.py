import sys

import time

while 1:

	sys.stdout.write(time.strftime('\r%Y-%m-%d %H:%M:%S'))

	sys.stdout.flush()