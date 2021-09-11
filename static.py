"""
Move static files from `source` which are not in the `_static` folder.
"""

import os
import pathlib
from distutils.dir_util import copy_tree
from colorama import Fore
from time import perf_counter

WARNING = Fore.LIGHTRED_EX
INFO = Fore.LIGHTCYAN_EX
SUCCESS = Fore.LIGHTGREEN_EX
RESET = Fore.RESET
HEADER = Fore.LIGHTBLUE_EX
TITLE = Fore.CYAN
__patterns__ = ['images']

print(f'{TITLE}Moving Static Directories{RESET}')
start = perf_counter()

path = os.path.abspath('./source')
print(f'{HEADER}INFO{RESET}: {INFO}Source Directory Used:{RESET}\n{path}')

build = os.path.abspath('./build/html')
print(f'{HEADER}INFO{RESET}: {INFO}Build Directory Used:{RESET}\n{path}')

found = list()
for pattern in __patterns__:
    current = list(pathlib.Path(path).rglob(f'**/{pattern}'))
    print(f'{HEADER}INFO{RESET}: {INFO}Appending {len(current)} directories which are named {pattern}{RESET}')
    for pth in current:
        found.append(pth)
    print(f'{HEADER}INFO{RESET}: {INFO}Finished appending {len(current)} directories, total of {len(found)} to move as of now.{RESET}')

print(f'{HEADER}INFO:{RESET}: {INFO}Found {len(found)} directories to move')

lastMove = perf_counter()
for pthObj in found:
    current = str(pthObj.absolute())
    pthExt = current[len(path):]
    newPth = build + pthExt

    print(f'{HEADER}INFO{RESET}: {INFO}Copying {RESET}{current}{INFO} to {RESET}{newPth}')
    
    if not os.path.isdir(newPth):
        print(f'{HEADER}INFO{RESET}: {INFO}Created new directory at:{RESET}\n{newPth}')

    try:
        ## copy_tree(current, newPth)

        # More info provided this way
        crntStart = perf_counter()
        for file in os.listdir(current):
            with open(current + f'\\{file}', 'rb') as r:
                with open(newPth + f'\\{file}', 'wb') as w:
                    w.write(r.read())
                    timeTaken = round((perf_counter() - crntStart) * 1000)
                    print(f'{HEADER}SUCCESS{RESET}: {SUCCESS}Copied {file} to{RESET}\n{newPth}\n{SUCCESS}In {timeTaken}ms{RESET}')

    except Exception as e:
        print(f'{HEADER}WARNING{RESET}: {WARNING}Failed to copy {RESET}{current}{INFO} to {RESET}{newPth}\n{WARNING}Errored out with {RESET}\n{e}')
    else:
        timeTaken = round((perf_counter() - lastMove) * 1000)
        print(f'{HEADER}SUCCESS{RESET}: {SUCCESS}Successfully moved directory in {timeTaken}ms{RESET}')
    lastMove = perf_counter()

timeTaken = round((perf_counter() - start) * 1000)
print(f'Ended proccess after {Fore.YELLOW}{timeTaken}{RESET}ms')
