Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l = [23,54,67,90,87,12,2,49,72]
l
[23, 54, 67, 90, 87, 12, 2, 49, 72]
type(l)
<class 'list'>
l.pop()
72
l
[23, 54, 67, 90, 87, 12, 2, 49]
l.pop()
49
l.pop()
2
l
[23, 54, 67, 90, 87, 12]
l.pop(0)
23
l
[54, 67, 90, 87, 12]
l.pop(2)
90
l
[54, 67, 87, 12]
l.remove(87)
l
[54, 67, 12]
l.remove(67)
l
[54, 12]
l.clear()
l
[]
l = [23,54,67,90,87,12,2,49,72]
l
SyntaxError: multiple statements found while compiling a single statement
l = [23,54,67,90,87,12,2,49,72]
l
[23, 54, 67, 90, 87, 12, 2, 49, 72]
l.count(67)
1
l.index(54)
1
l.index(2)
6
sorted(l)
[2, 12, 23, 49, 54, 67, 72, 87, 90]
l
[23, 54, 67, 90, 87, 12, 2, 49, 72]
l.sort()
l
[2, 12, 23, 49, 54, 67, 72, 87, 90]
l.reverse()
l
[90, 87, 72, 67, 54, 49, 23, 12, 2]
l.sort(reverse=True)
l
[90, 87, 72, 67, 54, 49, 23, 12, 2]
a = [1,2]
c = a
c
[1, 2]
a is c
True
c.append(3)
c
[1, 2, 3]
a
[1, 2, 3]
c.append(13)
c
[1, 2, 3, 13]
a
[1, 2, 3, 13]
b = a.copy()
b
[1, 2, 3, 13]
b.append(12)
b
[1, 2, 3, 13, 12]
a
[1, 2, 3, 13]
l
[90, 87, 72, 67, 54, 49, 23, 12, 2]
any(l)
True
l.append(0)
l
[90, 87, 72, 67, 54, 49, 23, 12, 2, 0]
any(l)
True
all(l)
False
k = [0,0.0,'']
k
[0, 0.0, '']
any(k)
False
all(k)
False
k.append(1)
k
[0, 0.0, '', 1]
anny(k)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    anny(k)
NameError: name 'anny' is not defined. Did you mean: 'any'?
any(k)
True
all(k)
False
sum(l)
456


'''Tuple'''
'Tuple'


t = ()
t = tuple()
t = tuple((1,2,3,4,5))
t
(1, 2, 3, 4, 5)
type(t)
<class 'tuple'>
t = 1,2,3,4,5
t
(1, 2, 3, 4, 5)
type(t)
<class 'tuple'>
t = (1)
t
1
type(t)
<class 'int'>
t = (1,)
t
(1,)
type(t)
<class 'tuple'>
t = (1,2,3,4,1,1,1,1,1,1,1)
t
(1, 2, 3, 4, 1, 1, 1, 1, 1, 1, 1)
t = (1,1.1,'dsdf', [1,2,3], {1,2,3}, (1,2,3,4), {1:2,3:4}, False, True)
t
(1, 1.1, 'dsdf', [1, 2, 3], {1, 2, 3}, (1, 2, 3, 4), {1: 2, 3: 4}, False, True)
t = (1,2,3,4)
t
(1, 2, 3, 4)
a,b,c,d = t
a
1
b
2
c

d
4
c
3
d
4
a,b,c = (1,2,3,4,5,5,6)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    a,b,c = (1,2,3,4,5,5,6)
ValueError: too many values to unpack (expected 3)
a,b,c = (1,2,3)
a
1
b
2
c
3
t = (1,1.1,'dsdf', [1,2,3], {1,2,3}, (1,2,3,4), {1:2,3:4}, False, True)

t
(1, 1.1, 'dsdf', [1, 2, 3], {1, 2, 3}, (1, 2, 3, 4), {1: 2, 3: 4}, False, True)
len(t)
9
t[3]
[1, 2, 3]
'''in case, there is a mutuable data types in the list, that can be change inside. '''
'in case, there is a mutuable data types in the list, that can be change inside. '
t[3].append(1)
t
(1, 1.1, 'dsdf', [1, 2, 3, 1], {1, 2, 3}, (1, 2, 3, 4), {1: 2, 3: 4}, False, True)
a = (1,2,3,4,5)
b = (7,8,9)
a+b
(1, 2, 3, 4, 5, 7, 8, 9)
a*2
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
t
(1, 1.1, 'dsdf', [1, 2, 3, 1], {1, 2, 3}, (1, 2, 3, 4), {1: 2, 3: 4}, False, True)
t[2]
'dsdf'
t[-1]
True
t[4]
{1, 2, 3}
t[3:6]
([1, 2, 3, 1], {1, 2, 3}, (1, 2, 3, 4))
t[::-1]
(True, False, {1: 2, 3: 4}, (1, 2, 3, 4), {1, 2, 3}, [1, 2, 3, 1], 'dsdf', 1.1, 1)
t[-2:]
(False, True)
t[-4:]
((1, 2, 3, 4), {1: 2, 3: 4}, False, True)
t
(1, 1.1, 'dsdf', [1, 2, 3, 1], {1, 2, 3}, (1, 2, 3, 4), {1: 2, 3: 4}, False, True)
1 int
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l in t
False
10 not in t
True
False not in t
False


'''Tuple Methods'''
'Tuple Methods'

len(t)
9
sorted(t)
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    sorted(t)
TypeError: '<' not supported between instances of 'str' and 'float'
t = (23,433,4,434,325,35,535,4534,545,45)
t
(23, 433, 4, 434, 325, 35, 535, 4534, 545, 45)
len(t)
10
sorted(t)
[4, 23, 35, 45, 325, 433, 434, 535, 545, 4534]
max(t)
4534
min(t)
4
count(23)
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    count(23)
NameError: name 'count' is not defined. Did you mean: 'round'?
t.count(23)
1
t.index(23)
0
any(t)
True
all(t)
True
t
(23, 433, 4, 434, 325, 35, 535, 4534, 545, 45)
sum(t)
6913
s = {}
type(s)
<class 'dict'>
s = set()
type(s)
<class 'set'>
s = {1,2,3,4}
s
{1, 2, 3, 4}
s = {65,87,6756,32,56,768,65,56,56}
ss
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    ss
NameError: name 'ss' is not defined. Did you mean: 's'?
s
{32, 65, 768, 6756, 87, 56}
s= {1,1,1,1,1,1,1}
s
{1}
s = set()
s.add6913
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    s.add6913
AttributeError: 'set' object has no attribute 'add6913'

s.add(1)
s
{1}
s.add(1.2)
s
{1, 1.2}
s.add('fdfs')
s
{1, 'fdfs', 1.2}
s.add(2+5j)
s
{(2+5j), 1, 'fdfs', 1.2}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    s.add([1,2,3])
TypeError: unhashable type: 'list'
s.add((1,2,3))
s
{1, 1.2, 'fdfs', (1, 2, 3), (2+5j)}
s.add({1:2,3:4})
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    s.add({1:2,3:4})
TypeError: unhashable type: 'dict'
s.add({1,2,3,4})
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    s.add({1,2,3,4})
TypeError: unhashable type: 'set'
s.add(False)
s
{False, 1, 1.2, 'fdfs', (1, 2, 3), (2+5j)}
a = {1,4,6,8}
b = {4,5,6,7,8,9}
a
{8, 1, 4, 6}
b
{4, 5, 6, 7, 8, 9}
a
{8, 1, 4, 6}
b
{4, 5, 6, 7, 8, 9}
a+b
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a*3
Traceback (most recent call last):
  File "<pyshell#179>", line 1, in <module>
    a*3
TypeError: unsupported operand type(s) for *: 'set' and 'int'
a[2]
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    a[2]
TypeError: 'set' object is not subscriptable
a[::-1]
Traceback (most recent call last):
  File "<pyshell#181>", line 1, in <module>
    a[::-1]
TypeError: 'set' object is not subscriptable
a
{8, 1, 4, 6}
b
{4, 5, 6, 7, 8, 9}
4 in a
True
7 not in a
True
a
{8, 1, 4, 6}
b
{4, 5, 6, 7, 8, 9}
a | b
{1, 4, 5, 6, 7, 8, 9}
a & b
{8, 4, 6}
a ^ b
{1, 5, 7, 9}
a-b
{1}
a
{8, 1, 4, 6}
b
{4, 5, 6, 7, 8, 9}
a.isdisjoint(b)
False
a.isdisjoint({99,100})
True
a
{8, 1, 4, 6}
{8}.issubset(a)
True
{100,99}.issubset(a)
False
a.issubset(b)
False
{1,2,3,4,5,6,7,8,9,10}.issuperset(a)
True
