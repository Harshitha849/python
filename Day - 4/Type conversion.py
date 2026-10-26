Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
a
10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
b = 10.0
b
10.0
int(b)
10
complex(b)
(10+0j)
str(b)
'10.0'
list(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
tuple(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
set(b)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
dict(b)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
bool(b)
True
c = 2 + 5j
c
(2+5j)
int(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(c)
'(2+5j)'
list(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
dict(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
set(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
tuple(c)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
bool(c)
True
d = "Codegnan"
d
'Codegnan'
int(d)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'Codegnan'
float(d)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(d)
ValueError: could not convert string to float: 'Codegnan'
complex(d)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    complex(d)
ValueError: complex() arg is a malformed string
list(d)
['C', 'o', 'd', 'e', 'g', 'n', 'a', 'n']
set(d)
{'n', 'a', 'C', 'd', 'o', 'e', 'g'}
tuple(d)
('C', 'o', 'd', 'e', 'g', 'n', 'a', 'n')
dict(d)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(d)
True
e = '1234'
int(e)
1234
float(e)
1234.0
complex(e)
(1234+0j)
list(e)
['1', '2', '3', '4']
tuple(e)
('1', '2', '3', '4')
dict(e)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    dict(e)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(e)
True
set(e)
{'1', '3', '2', '4'}
f = [1,2,3,4]
f
[1, 2, 3, 4]
int(f)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    int(f)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(f)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    float(f)
TypeError: float() argument must be a string or a real number, not 'list'
complex(f)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    complex(f)
TypeError: complex() first argument must be a string or a number, not 'list'
tuple(f)
(1, 2, 3, 4)
set(f)
{1, 2, 3, 4}
dict(f)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    dict(f)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(f)
True
str(f)
'[1, 2, 3, 4]'
g = (1,2,3,4)
g
(1, 2, 3, 4)
int(g)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    int(g)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(f)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    float(f)
TypeError: float() argument must be a string or a real number, not 'list'
complex(g)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    complex(g)
TypeError: complex() first argument must be a string or a number, not 'tuple'
type(g)
<class 'tuple'>
str(g)
'(1, 2, 3, 4)'
list(g)
[1, 2, 3, 4]
set(g)
{1, 2, 3, 4}
dict(g)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    dict(g)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(g)
True
h = {1,2,3,4}
type(h)
<class 'set'>
h
{1, 2, 3, 4}
int(h)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    int(h)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(h)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    float(h)
TypeError: float() argument must be a string or a real number, not 'set'
complex(g)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    complex(g)
TypeError: complex() first argument must be a string or a number, not 'tuple'
complex(h)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    complex(h)
TypeError: complex() first argument must be a string or a number, not 'set'
str(h)
'{1, 2, 3, 4}'
list(h)
[1, 2, 3, 4]
tuple(h)
(1, 2, 3, 4)
dict(h)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    dict(h)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(h)
True
i = {1:2, 2:3, 3:4, 5:6}
type(i)
<class 'dict'>
i
{1: 2, 2: 3, 3: 4, 5: 6}
int(i)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    int(i)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(i)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    float(i)
TypeError: float() argument must be a string or a real number, not 'dict'
complex(i)
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    complex(i)
TypeError: complex() first argument must be a string or a number, not 'dict'
str(i)
'{1: 2, 2: 3, 3: 4, 5: 6}'
list(i)
[1, 2, 3, 5]
tuple(i)
(1, 2, 3, 5)
set(i)
{1, 2, 3, 5}
bool(i)
True
j = 0
type(j)
<class 'int'>
j = True
j
True
int(j)
1
float(j)
1.0
complex(j)
(1+0j)
str(j)
'True'
list(j)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    list(j)
TypeError: 'bool' object is not iterable
tuple(j)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    tuple(j)
TypeError: 'bool' object is not iterable
set(j)
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    set(j)
TypeError: 'bool' object is not iterable
dict(j)
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    dict(j)
TypeError: 'bool' object is not iterable
