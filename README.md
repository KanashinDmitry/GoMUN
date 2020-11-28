# GoMUN
## Multiplication of non-zero numbers
Just another unrestricted and context-sensitive grammars generating correct multiplication operation under unary integers.

Result grammars can be found in [Unrestricted grammar](https://github.com/KanashinDmitry/GoMUN/blob/main/res_grammar_0.txt) and [Context-sensitive grammar](https://github.com/KanashinDmitry/GoMUN/blob/main/res_grammar_1.txt)

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
Some results with full derivation can be found in [Unrestricted grammar results](https://github.com/KanashinDmitry/GoMUN/blob/main/res_cons_t0.txt) and [Context-sensitive grammar results](https://github.com/KanashinDmitry/GoMUN/blob/main/res_cons_t1.txt)

3*2=6
```
python3 main.py -l=3 -r=2 --res=6 -t=0
111*11=111111 True
```

3*2=5
```
python3 main.py -l=3 -r=2 --res=5 -t=0
111*11=11111 False
```

2*2=4 with derivation on Unrestricted grammar
```
11*11=1111 ['1', '1', '*', '1', '1', '=', '1', '1', '1', '1']
Start symbol S
Using S -> S1 Q0 S2 new sentence is ['S1', 'Q0', 'S2']
Using S2 -> V5 S2 new sentence is ['B', 'Q0', 'V5', 'S2']
Using S2 -> V5 S2 new sentence is ['B', 'Q0', 'V5', 'V5', 'S2']
Using S2 -> V18 S2 new sentence is ['B', 'Q0', 'V5', 'V5', 'V18', 'S2']
...
Using S2 -> S3 new sentence is ['B', 'Q0', 'V5', 'V5', 'V18', 'V5', 'V5', 'V14', 'V5', 'V5', 'V5', 'V5', 'S3']
Using S3 -> B new sentence is ['B', 'Q0', 'V5', 'V5', 'V18', 'V5', 'V5', 'V14', 'V5', 'V5', 'V5', 'V5', 'B']
Using Q0 V5 -> V4 Q1 new sentence is ['B', 'V4', 'Q1', 'V5', 'V18', 'V5', 'V5', 'V14', 'V5', 'V5', 'V5', 'V5', 'B']
Using Q1 V5 -> V5 Q1 new sentence is ['B', 'V4', 'V5', 'Q1', 'V18', 'V5', 'V5', 'V14', 'V5', 'V5', 'V5', 'V5', 'B']
Using Q1 V18 -> V18 Q2 new sentence is ['B', 'V4', 'V5', 'V18', 'Q2', 'V5', 'V5', 'V14', 'V5', 'V5', 'V5', 'V5', 'B']
Using Q2 V5 -> V5 Q3 new sentence is ['B', 'V4', 'V5', 'V18', 'V5', 'Q3', 'V5', 'V14', 'V5', 'V5', 'V5', 'V5', 'B']
Using Q3 V5 -> V5 Q3 new sentence is ['B', 'V4', 'V5', 'V18', 'V5', 'V5', 'Q3', 'V14', 'V5', 'V5', 'V5', 'V5', 'B']
Using Q3 V14 -> V14 Q7 new sentence is ['B', 'V4', 'V5', 'V18', 'V5', 'V5', 'V14', 'Q7', 'V5', 'V5', 'V5', 'V5', 'B']
Using Q7 V5 -> V5 Q8 new sentence is ['B', 'V4', 'V5', 'V18', 'V5', 'V5', 'V14', 'V5', 'Q8', 'V5', 'V5', 'V5', 'B']
...
Using Q2 V3 -> V3 Q4 new sentence is ['B', 'V4', 'V5', 'V18', 'V3', 'Q4', 'V3', 'V14', 'V3', 'V3', 'V3', 'V3', 'B']
Using Q4 V3 -> V3 Q4 new sentence is ['B', 'V4', 'V5', 'V18', 'V3', 'V3', 'Q4', 'V14', 'V3', 'V3', 'V3', 'V3', 'B']
Using Q4 V14 -> V14 Q5 new sentence is ['B', 'V4', 'V5', 'V18', 'V3', 'V3', 'V14', 'Q5', 'V3', 'V3', 'V3', 'V3', 'B']
Using V14 Q5 V3 -> Q6 V14 V3 new sentence is ['B', 'V4', 'V5', 'V18', 'V3', 'V3', 'Q6', 'V14', 'V3', 'V3', 'V3', 'V3', 'B']
Using Q6 V14 -> Q6 = Q6 new sentence is ['B', 'V4', 'V5', 'V18', 'V3', 'V3', 'Q6', '=', 'Q6', 'V3', 'V3', 'V3', 'V3', 'B']
Using V3 Q6 -> Q6 1 Q6 new sentence is ['B', 'V4', 'V5', 'V18', 'V3', 'Q6', '1', 'Q6', '=', 'Q6', 'V3', 'V3', 'V3', 'V3', 'B']
Using V3 Q6 -> Q6 1 Q6 new sentence is ['B', 'V4', 'V5', 'V18', 'Q6', '1', 'Q6', '1', 'Q6', '=', 'Q6', 'V3', 'V3', 'V3', 'V3', 'B']
Using V18 Q6 -> Q6 * Q6 new sentence is ['B', 'V4', 'V5', 'Q6', '*', 'Q6', '1', 'Q6', '1', 'Q6', '=', 'Q6', 'V3', 'V3', 'V3', 'V3', 'B']
Using Q6 V3 -> Q6 1 Q6 new sentence is ['B', 'V4', 'V5', 'Q6', '*', 'Q6', '1', 'Q6', '1', 'Q6', '=', 'Q6', '1', 'Q6', 'V3', 'V3', 'V3', 'B']
Using Q6 V3 -> Q6 1 Q6 new sentence is ['B', 'V4', 'V5', 'Q6', '*', 'Q6', '1', 'Q6', '1', 'Q6', '=', 'Q6', '1', 'Q6', '1', 'Q6', 'V3', 'V3', 'B']
Using Q6 V3 -> Q6 1 Q6 new sentence is ['B', 'V4', 'V5', 'Q6', '*', 'Q6', '1', 'Q6', '1', 'Q6', '=', 'Q6', '1', 'Q6', '1', 'Q6', '1', 'Q6', 'V3', 'B']
...
Using Q6 -> eps new sentence is ['1', '1', '*', '1', '1', '=', '1', '1', 'Q6', '1', 'Q6', '1', 'Q6', 'Q6']
Using Q6 -> eps new sentence is ['1', '1', '*', '1', '1', '=', '1', '1', '1', 'Q6', '1', 'Q6', 'Q6']
Using Q6 -> eps new sentence is ['1', '1', '*', '1', '1', '=', '1', '1', '1', '1', 'Q6', 'Q6']
Using Q6 -> eps new sentence is ['1', '1', '*', '1', '1', '=', '1', '1', '1', '1', 'Q6']
Using Q6 -> eps new sentence is ['1', '1', '*', '1', '1', '=', '1', '1', '1', '1']
```
