#!/usr/bin/env python
""""hexview v1.00"""

import argparse
import math
import shutil


parser = argparse.ArgumentParser(add_help=True, description="This is an experimental hex viewer.")
parser.add_argument("file", action="store", help="Input file name.")
parser.add_argument("-g", action="store_true", default=False, help="Enable grid lines.")
parser.add_argument("-c", action="store_true", default=False, help="Enable color.")
parser.add_argument("-d", action="store_true", default=False, help="Enable debug output.")

pargs = parser.parse_args()

with open(pargs.file, "rb") as f:
    data = f.read()

c, r = shutil.get_terminal_size()

if pargs.c:
    colors = [31, 32, 33, 34, 35, 36, 37]
elif not pargs.c:
    colors = [37 for i in range(7)]

if not pargs.g:
    n = int(c / 3)
    rs = math.ceil(len(data) * 3 / c)
    i = 0
    cc = 0
    for j in range(rs):
        line = []
        for k in range(n):
            try:
                byt = hex(data[i])[2:]
                buff = " " * (3 - len(byt))
                line.append(f"\u001b[{colors[cc]}m{buff}{byt}")
            except IndexError:
                pass
            i += 1
            cc += 1
            if cc % 7 == 0:
                cc = 0
        if k == n - 1:
            cc = 0
        print("".join(line))
        i += 1

elif pargs.g:
    n = int(c / 5)
    rs = math.ceil(len(data) * 5 / c) # rounding up causing extra blank rows on long outputs
    print(f"┌{'────┬' * int(n - 1)}───┐")
    i = 0
    cc = 0
    for j in range(rs):
        line = []
        for k in range(n):
            try:
                byt = hex(data[i])[2:]
                buff = " " * (3 - len(byt))
                line.append(f"\u001b[37m│\u001b[{colors[cc]}m{buff}{byt}\u001b[37m ")
            except IndexError:
                line.append("│    ")
            i += 1
            cc += 1
            if cc % 7 == 0:
                cc = 0
        if k == n - 1:
            cc = 0
        line[-1] = line[-1][:-1] + "│"
        print("".join(line))
        print(f"├{'────┼' * int(n - 1)}───┤")
        i += 1
    print(f"\033[1A{chr(9492)}{'────┴' * int(n - 1)}───┘")

if pargs.d:
    print(f"DEBUG:\nc, r {c}, {r}\nn {n}\nrs {rs}\ni {i}\ncc {cc}")
