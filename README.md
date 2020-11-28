# GoMUN
## Multiplication of non-zero numbers
Just another unrestricted and context-sensitive grammars generating correct multiplication operation under unary integers.

Result grammars can be found in [Unrestricted grammar](https://github.com/KanashinDmitry/GoMUN/blob/dev/GrammarType0.py) and [Context-sensitive grammar](https://github.com/KanashinDmitry/GoMUN/blob/dev/GrammarType1.py)

## Usage
```
usage: main.py [-h] -l LEFT -r RIGHT --res RESULT [--der] [--path RES_PATH] -t TYPE

Correctness of multiplication expression

optional arguments:
  -h, --help       show this help message and exit
  -l LEFT          left integer in sum
  -r RIGHT         right integer in sum
  --res RESULT     result integer in sum
  --der            get derivation
  --path RES_PATH  path of file where derivation will be written
  -t TYPE          Grammar type (0 or 1)
```
## Examples
