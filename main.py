a1 = '''
 (-_-) 
_/|__|\\_
  |  |
'''
a2 = '''
  (-_-) 
_/|__|\\_
  |  |
'''

from time import sleep
import os
from sys import stderr

flag = True
while True:
    if os.name == 'posix':  # POSIX
        os.system('clear')
    elif os.name == 'nt':  # Windows
        os.system('cls')
    else:
        print('ERROR: Unsupported Operating System.\nPlease report this issue at: https://github.com/eswar-7116/vibr', file=stderr)
        exit(2)

    if flag:
        print(a1)
    else:
        print(a2)
    flag = not flag
    sleep(0.3)

