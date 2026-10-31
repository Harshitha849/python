Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = {34, 8, 40, 12, 13, 50, 56, 90, 29}
s
{34, 8, 40, 12, 13, 50, 56, 90, 29}
sorted(s)
[8, 12, 13, 29, 34, 40, 50, 56, 90]
len(s)
9
min(s)
8
max(s)
90
sum(s)
332
any(s)
True
all(s)
True
s.add(10)
s
{34, 8, 40, 10, 12, 13, 50, 56, 90, 29}
s.add(100)
s
{34, 100, 8, 40, 10, 12, 13, 50, 56, 90, 29}
s.update({1,20,30})
s
{1, 34, 100, 8, 40, 10, 12, 13, 50, 20, 56, 90, 29, 30}
s.pop()
1
s.pop()
34
s.pop()
100
s
{8, 40, 10, 12, 13, 50, 20, 56, 90, 29, 30}
s.remove(40)
s.remove(10)
s
{8, 12, 13, 50, 20, 56, 90, 29, 30}
s.discard(50)
s
{8, 12, 13, 20, 56, 90, 29, 30}
s.discard(50)
s
{8, 12, 13, 20, 56, 90, 29, 30}
s.remove(40)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s.remove(40)
KeyError: 40
s.clear()
s
set()
a = {1,2,3,4,5}
a
{1, 2, 3, 4, 5}
b = a
a
{1, 2, 3, 4, 5}
b
{1, 2, 3, 4, 5}
b.add(7)
b
{1, 2, 3, 4, 5, 7}
a
{1, 2, 3, 4, 5, 7}
c = a.copy()
c.add(20)
c
{1, 2, 3, 4, 5, 20, 7}
a
{1, 2, 3, 4, 5, 7}


'''Dict'''
'Dict'

d = {}
d = {1:1,1:2}
d
{1: 2}
d = {1:2,3:4}
d
{1: 2, 3: 4}
type(d)
<class 'dict'>
d
{1: 2, 3: 4}
d = {}
d[1] = 'int'
d
{1: 'int'}
d[1.1] = 'float'
d
{1: 'int', 1.1: 'float'}
d['str'] = 'str'
d
{1: 'int', 1.1: 'float', 'str': 'str'}
d[2+5j]
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    d[2+5j]
KeyError: (2+5j)
d[2+5j] = 'com'
d
{1: 'int', 1.1: 'float', 'str': 'str', (2+5j): 'com'}
d[(1,2,3)] = 'tuple'
d
{1: 'int', 1.1: 'float', 'str': 'str', (2+5j): 'com', (1, 2, 3): 'tuple'}
d[False] = 'bool'
d
{1: 'int', 1.1: 'float', 'str': 'str', (2+5j): 'com', (1, 2, 3): 'tuple', False: 'bool'}
d[[1,2,3]] = 'list'
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    d[[1,2,3]] = 'list'
TypeError: unhashable type: 'list'
d[{1,2,3}] = 'set'
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    d[{1,2,3}] = 'set'
TypeError: unhashable type: 'set'
d[{1:2, 3:4}] = 'dict'
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    d[{1:2, 3:4}] = 'dict'
TypeError: unhashable type: 'dict'
d
{1: 'int', 1.1: 'float', 'str': 'str', (2+5j): 'com', (1, 2, 3): 'tuple', False: 'bool'}
d[1] = 1
d
{1: 1, 1.1: 'float', 'str': 'str', (2+5j): 'com', (1, 2, 3): 'tuple', False: 'bool'}
d.clear()
d
{}
d[1] = 1
d[2] = 12.2
d[3] = 23+3j
d[4] = 'str'
d[5] = [1,2]
d[6] = (1,2)
d[7] = {1,2}
d[8] = {1:1, 2:2}
d[9] = False
d
{1: 1, 2: 12.2, 3: (23+3j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 1, 2: 2}, 9: False}
d[10] = 1
d[11] = 1
d[12] = 1
d
{1: 1, 2: 12.2, 3: (23+3j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: {1: 1, 2: 2}, 9: False, 10: 1, 11: 1, 12: 1}
d[2]
12.2
d[10]
1
d[4]
'str'
d[6]
(1, 2)
d[8]
{1: 1, 2: 2}
d[13]
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    d[13]
KeyError: 13
d.get(13)
d.get(7)
{1, 2}
d.get(18)
KeyboardInterrupt
d.get(18, 'key is not there')
'key is not there'
d.get(7, 'key is not there')
{1, 2}
d.get(30, 'key is not there')
'key is not there'
'str' in d
False
1 in d
True
[1,2] in d
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    [1,2] in d
TypeError: unhashable type: 'list'
12.2 in d
False
12 in d
True
d[8] = 'dict'
d
{1: 1, 2: 12.2, 3: (23+3j), 4: 'str', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1}
d[3] = 23
d
{1: 1, 2: 12.2, 3: 23, 4: 'str', 5: [1, 2], 6: (1, 2), 7: {1, 2}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1}
d[5] = 3
d
{1: 1, 2: 12.2, 3: 23, 4: 'str', 5: 3, 6: (1, 2), 7: {1, 2}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1}
d[13] = 100
d
{1: 1, 2: 12.2, 3: 23, 4: 'str', 5: 3, 6: (1, 2), 7: {1, 2}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1, 13: 100}
d[14] = 200
d
{1: 1, 2: 12.2, 3: 23, 4: 'str', 5: 3, 6: (1, 2), 7: {1, 2}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1, 13: 100, 14: 200}
d.update({15:500, 16:600})
d
{1: 1, 2: 12.2, 3: 23, 4: 'str', 5: 3, 6: (1, 2), 7: {1, 2}, 8: 'dict', 9: False, 10: 1, 11: 1, 12: 1, 13: 100, 14: 200, 15: 500, 16: 600}
d.pop(2)
12.2
d.pop(12)
1
d
{1: 1, 3: 23, 4: 'str', 5: 3, 6: (1, 2), 7: {1, 2}, 8: 'dict', 9: False, 10: 1, 11: 1, 13: 100, 14: 200, 15: 500, 16: 600}
del d[5]
d
{1: 1, 3: 23, 4: 'str', 6: (1, 2), 7: {1, 2}, 8: 'dict', 9: False, 10: 1, 11: 1, 13: 100, 14: 200, 15: 500, 16: 600}
del d[8]
d
{1: 1, 3: 23, 4: 'str', 6: (1, 2), 7: {1, 2}, 9: False, 10: 1, 11: 1, 13: 100, 14: 200, 15: 500, 16: 600}
d.clear()
d
{}
d
{1: 1, 3: 23, 4: 'str', 6: (1, 2), 7: {1, 2}, 9: False, 10: 1, 11: 1, 13: 100, 14: 200, 15: 500, 16: 600}
SyntaxError: multiple statements found while compiling a single statement
d = {1: 1, 3: 23, 4: 'str', 6: (1, 2), 7: {1, 2}, 9: False, 10: 1, 11: 1, 13: 100, 14: 200, 15: 500, 16: 600}
d.keys()
dict_keys([1, 3, 4, 6, 7, 9, 10, 11, 13, 14, 15, 16])
d.values()
dict_values([1, 23, 'str', (1, 2), {1, 2}, False, 1, 1, 100, 200, 500, 600])
d.items()
dict_items([(1, 1), (3, 23), (4, 'str'), (6, (1, 2)), (7, {1, 2}), (9, False), (10, 1), (11, 1), (13, 100), (14, 200), (15, 500), (16, 600)])
len(d)
12
sorted(d)
[1, 3, 4, 6, 7, 9, 10, 11, 13, 14, 15, 16]
min(d)
1
max(d)
16
d
{1: 1, 3: 23, 4: 'str', 6: (1, 2), 7: {1, 2}, 9: False, 10: 1, 11: 1, 13: 100, 14: 200, 15: 500, 16: 600}
a = {1:2, 2:2}
b = a
b[3] = 3
a
{1: 2, 2: 2, 3: 3}
b
{1: 2, 2: 2, 3: 3}
c = a.copy()
c[4] = 4
c
{1: 2, 2: 2, 3: 3, 4: 4}
a
{1: 2, 2: 2, 3: 3}
d = dict.fromkeys(["a", "b", "c", "d", "e"], 0)
d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
d.setdefault('a')
0
d.setdefault('h')
d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None}
d.setdefault('k', 1)
1
d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None, 'k': 1}
d.setdefault('c', 1)
0
d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'h': None, 'k': 1}
s = frozenset({1,2,3,4})
s
frozenset({1, 2, 3, 4})
len(s)
4
max(s)
4
min(s)
1
type(s)
<class 'frozenset'>
