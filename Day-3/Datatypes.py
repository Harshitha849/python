Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 10
type(a)
<class 'int'>
b = 12.5
type(b)
<class 'float'>
c = 2+5j
c
(2+5j)
type(c)
<class 'complex'>
s = "codegnan"
s
'codegnan'
type(s)
<class 'str'>
l = [1,2,3,4]
type(l)
<class 'list'>
k = [1,23.4m"4565",[1,2,3]]
SyntaxError: invalid decimal literal
k = [1,23.4,"4565",[1,2,3]]
k
[1, 23.4, '4565', [1, 2, 3]]
type(k)
<class 'list'>
l = [1,1,1,1]
l
[1, 1, 1, 1]
type(l)
<class 'list'>
s = "code"
s
'code'
id(s)
1700184457520
s += "gnan"
s
'codegnan'
id(s)
1700190241712
l = [1,2,3]
l
[1, 2, 3]
id(l)
1700221635904
l.append(12)
l
[1, 2, 3, 12]
id(1)
1700183998704
l.pop()
12
;
SyntaxError: invalid syntax
l
[1, 2, 3]
id(l)
1700221635904
t = (1,2,3,4)
t
(1, 2, 3, 4)
t= (1,1,1,1)
t
(1, 1, 1, 1)
t = (1,2.3)
t
(1, 2.3)
type(t)
<class 'tuple'>
s = {34, 1234, 124321, 1325, 235, 34, 34, 34, 34, 34}
s
{124321, 34, 1234, 235, 1325}
type(s)
<class 'set'>
d = {1:"one", 2:4, 3:[1,2,3], 5:(1,23)]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
d = {1:"one", 2:4, 3:[1,2,3], 5:(1,23)}
d
{1: 'one', 2: 4, 3: [1, 2, 3], 5: (1, 23)}
pro = {"pro_name": "laptop", "price": 55000, "discount" : 10}
pro
{'pro_name': 'laptop', 'price': 55000, 'discount': 10}
type(pro)
<class 'dict'>
type(d)
<class 'dict'>
s = False
type(s)
<class 'bool'>
s = None
type(s)
<class 'NoneType'>
