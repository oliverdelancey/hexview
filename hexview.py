#!/usr/bin/env python
"""hexview v2.00 @ Oliver Sandli 2020"""

import argparse
import shutil


def roundu(x: int, y: int, z: int) -> int:
    """Run calculation, round up, and return result."""
    w = x * y / z
    iw = int(w)
    if iw - w != 0:
        return iw + 1
    return iw


parser = argparse.ArgumentParser(
    add_help=True,
    formatter_class=argparse.RawTextHelpFormatter,
    description="hexview v2.00 Copyright Oliver Sandli 2020"
    )
parser.add_argument(
    "file",
    action="store",
    help="Input file name."
    )
parser.add_argument(
    "-g",
    action="store_true",
    default=False,
    help="Enable grid lines."
    )
parser.add_argument(
    "-c",
    action="store_true",
    default=False,
    help="Enable color."
    )
parser.add_argument(
    "-f",
    action="store",
    help="""Output file in format of choice.
    csv
    html
    markdown
    txt"""
    )
parser.add_argument(
    "-d",
    action="store_true",
    default=False,
    help="Enable debug output (currently inactive)."
    )

pargs = parser.parse_args()

with open(pargs.file, "rb") as f:
    data = f.read()

c, r = shutil.get_terminal_size()

if pargs.c:
    colors = [31, 32, 33, 34, 35, 36, 37]
elif not pargs.c:
    colors = [37 for i in range(7)]
if pargs.f:
    if pargs.f == "csv":
        rs = roundu(len(data), 1, 16)
        i = 0
        stop = False
        with open(f"{pargs.file.split('.')[0]}.csv", "w") as f:
            f.write("00,01,02,03,04,05,06,07,08,09,0A,0B,0C,0D,0E,0F")
            for j in range(rs):
                line = []
                for k in range(16):
                    try:
                        line.append(hex(data[i])[2:])
                    except IndexError:
                        stop = True
                    i += 1
                l_s = str(line)[1:-1].replace("'", "").replace(" ", "")
                f.write(f"\n{l_s}")
                i += 1
                if stop:
                    break
    elif pargs.f == "html":
        rs = roundu(len(data), 1, 16)
        i = 0
        stop = False
        ht = """<table border='1'>
    <tr>
        <th></th>
        <th>00</th>
        <th>01</th>
        <th>02</th>
        <th>03</th>
        <th>04</th>
        <th>05</th>
        <th>06</th>
        <th>07</th>
        <th>08</th>
        <th>09</th>
        <th>0A</th>
        <th>0B</th>
        <th>0C</th>
        <th>0D</th>
        <th>0E</th>
        <th>0F</th>
    </tr>\n"""
        for j in range(rs):
            ht += f"\t<tr>\n\t\t<th>{hex(j)[2:]}</th>\n"
            for k in range(16):
                try:
                    ht += f"\t\t<td>{hex(data[i])[2:]}</td>\n"
                except IndexError:
                    ht += "\t\t<td></td>\n"
                    stop = True
                i += 1
            ht += "\t</tr>\n"
            i += 1
            if stop:
                break
        ht += "</table>\n"
        with open(f"{pargs.file.split('.')[0]}.htm", "w") as f:
            f.write(ht)
    elif pargs.f == "markdown":
        rs = roundu(len(data), 1, 16)
        i = 0
        stop = False
        md = """|  | 00 | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 0A | 0B | 0C | 0D | 0E | 0F |
| -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
"""
        for j in range(rs):
            line = [f"| {hex(j)[2:]} |"]
            for k in range(16):
                try:
                    line.append(f" {hex(data[i])[2:]} |")
                except IndexError:
                    stop = True
                i += 1
            md += f"{''.join(line)}\n"
            i += 1
            if stop:
                break
        with open(f"{pargs.file.split('.')[0]}.md", "w") as f:
            f.write(md)
    elif pargs.f == "txt":
        rs = roundu(len(data), 1, 16)
        cb = len(hex(rs)[2:])
        i = 0
        stop = False
        txt = f"┌{'─' * (cb + 2)}┬{'────┬' * 15}───┐\n│ {' ' * cb} │ 00 │ 01 │ 02 │ 03 │ 04 │ 05 │ 06 │ 07 │ 08 │ 09 │ 0A │ 0B │ 0C │ 0D │ 0E │ 0F│\n"
        txt += f"├{'─' * (cb + 2)}┼{'────┼' * 15}───┤\n"
        for j in range(rs):
            byt = hex(j)[2:]
            buff = " " * (cb + 1 - len(byt))
            line = [f"│{buff}{byt} "]
            for k in range(16):
                try:
                    byt = hex(data[i])[2:]
                    buff = " " * (3 - len(byt))
                    line.append(f"│{buff}{byt} ")
                except IndexError:
                    line.append("│    ")
                    stop = True
                i += 1
            line[-1] = line[-1][:-1] + "│\n"
            txt += "".join(line)
            i += 1
            if stop:
                break
            txt += f"├{'─' * (cb + 2)}┼{'────┼' * 15}───┤\n"
        txt += f"└{'─' * (cb + 2)}┴{'────┴' * 15}───┘\n"
        with open(f"{pargs.file.split('.')[0]}.txt", "w") as f:
            f.write(txt)
elif not pargs.f:
    if pargs.g:
        n = int(c / 5)
        rs = roundu(len(data), 5, c)
        print(f"┌{'────┬' * int(n - 1)}───┐")
        i = 0
        cc = 0
        stop = False
        for j in range(rs):
            line = []
            for k in range(n):
                try:
                    byt = hex(data[i])[2:]
                    buff = " " * (3 - len(byt))
                    line.append(f"\u001b[37m│\u001b[{colors[cc]}m{buff}{byt}\u001b[37m ")
                except IndexError:
                    line.append("│    ")
                    stop = True
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
            if stop:
                break
        print(f"\033[1A{chr(9492)}{'────┴' * int(n - 1)}───┘")
    elif not pargs.g:
        n = int(c / 3)
        rs = roundu(len(data), 3, c)
        i = 0
        cc = 0
        stop = False
        for j in range(rs):
            line = []
            for k in range(n):
                try:
                    byt = hex(data[i])[2:]
                    buff = " " * (3 - len(byt))
                    line.append(f"\u001b[{colors[cc]}m{buff}{byt}")
                except IndexError:
                    stop = True
                i += 1
                cc += 1
                if cc % 7 == 0:
                    cc = 0
            if k == n - 1:
                cc = 0
            print("".join(line))
            i += 1
            if stop:
                break
