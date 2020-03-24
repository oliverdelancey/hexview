# hexview

hexview is a command line hex viewer, outputting either to the terminal or a formatted table.

### Sample Terminal Output

with `-g` option.

```
┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬───┐   
│ 23 │ 21 │ 2f │ 75 │ 73 │ 72 │ 2f │ 62 │ 69 │ 6e │ 2f │ 65 │ 6e│   
├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼───┤   
│ 20 │ 70 │ 79 │ 74 │ 68 │ 6f │ 6e │ 33 │  a │ 22 │ 22 │ 22 │ 61│   
├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼───┤   
│ 74 │ 65 │ 73 │ 74 │ 20 │ 70 │ 79 │ 74 │ 68 │ 6f │ 6e │ 20 │ 66│   
├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼───┤   
│ 6c │ 65 │ 22 │ 22 │ 22 │  a │  a │ 64 │ 65 │ 66 │ 20 │ 73 │ 75│   
├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼───┤   
│ 5f │ 6c │ 69 │ 73 │ 74 │ 28 │ 6c │ 3a │ 20 │ 6c │ 69 │ 73 │ 74│   
├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼───┤   
│ 20 │ 2d │ 3e │ 20 │ 6c │ 69 │ 73 │ 74 │ 3a │  a │ 20 │ 20 │ 20│   
├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼───┤   
│ 6c │ 3a │ 20 │ 7b │ 73 │ 7d │ 22 │ 29 │  a │    │    │    │   │   
└────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴────┴───┘
```

### Requirements

* Python 3.6 or later (3.5 for type hints, 3.6 for f strings)

* A terminal that supports ANSI escape codes / colors if terminal output is desired

### Help

Run for help:
```bash
python hexview.py -h
```
```
usage: hexview.py [-h] [-g] [-c] [-f F] [-d] file

hexview v2.00 @ Oliver Sandli 2020

positional arguments:
  file        Input file name.

optional arguments:
  -h, --help  show this help message and exit
  -g          Enable grid lines.
  -c          Enable color.
  -f F        Output file in format of choice.
                      csv
                      html
                      markdown
                      txt
  -d          Enable debug output (currently inactive).
```
