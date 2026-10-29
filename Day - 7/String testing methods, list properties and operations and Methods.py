Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = "Python Programming"
s
'Python Programming'
s.startswith('p')
False
s.startswith('P')
True
s.startswith("Pyt")
True
s.endswith("img")
False
s.endswith("ing")
True
's'.islower()
True
'S'.islower()
False
'S'.isupper()
True
's'.isupper()
False
'codegnan@'.isalpha()
False
'code12'.isaplha()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    'code12'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
'cose12'.isalpha()
False
'code'.isalpha()
True
'code123'.isalnum()
True
'code@123'.isalnum()
False
'code'.isalnum()
True
s
'Python Programming'
s.istitle()
True
'myvar'.isidentifier()
True
'my@var'.isidentifier()
False
' '.isspace()
True
'                           helllo'.isspace()
False
'1243'.isdigit()
True
'1234'.isdecimal()
True
'1234'.isnumeric()
True
'a b c d'.split()
['a', 'b', 'c', 'd']
'a,b,c,d'.split()
['a,b,c,d']
'a,b,c,d'.split(',')
['a', 'b', 'c', 'd']
'a-b-c-d'.split(-)
SyntaxError: invalid syntax
'a-b-c-d'.split('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.split('-',2)
['a', 'b', 'c-d']
'a-b-c-d'.rsplit('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.rsplit('-')
['a', 'b', 'c', 'd']
'a-b-c-d'.rsplit('-',2)
['a-b', 'c', 'd']
s = """
Hello
world
python
"""
s
'\nHello\nworld\npython\n'
s.splitlines()
['', 'Hello', 'world', 'python']
l = ['a','b','c','d']
l
['a', 'b', 'c', 'd']
'-'.join(l)
'a-b-c-d'
'@'.join(l)
'a@b@c@d'
'*'.join(l)
'a*b*c*d'
'_'.join(l)
'a_b_c_d'
''.join(l)
'abcd'
s = 'a-b-c-d'
s
'a-b-c-d'
s.partition('b')
('a-', 'b', '-c-d')
'python.py'.parition('.')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    'python.py'.parition('.')
AttributeError: 'str' object has no attribute 'parition'. Did you mean: 'partition'?
'python.py'.partition('.')
('python', '.', 'py')
'pyt.hon.py'.partition('.')
('pyt', '.', 'hon.py')
'pyt.hon.py'.rpartition('.')
('pyt.hon', '.', 'py')
s = "hello"
s
'hello'
s.encode()
b'hello'
t = "Hello 😊"
t
'Hello 😊'
t.encode()
b'Hello \xf0\x9f\x98\x8a'
t.encode()
b'Hello \xf0\x9f\x98\x8a'
t.decode()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    t.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
b'Hello \xf0\x9f\x98\x8a'.decode()
'Hello 😊'


l = []
l = list()
l = [1,2,3]
l
[1, 2, 3]
l = list([1,2,3,4])
l
[1, 2, 3, 4]
type(l)
<class 'list'>
l = [2,3,4,5,5,6]
l
[2, 3, 4, 5, 5, 6]
l = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
l
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
l = [1,12.2,3+5j,"str",[1,2],(1,2),{1,2},{1:2},False,None]
l
[1, 12.2, (3+5j), 'str', [1, 2], (1, 2), {1, 2}, {1: 2}, False, None]
'''list operations'''
'list operations'
[1,2,3] + [4,5,6]
[1, 2, 3, 4, 5, 6]
[1,2,3] * 5
[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
l = ['python', 'java', 'c', 'flask', 'fastapi', 'mysql']
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql']
l[0]
'python'
l[-1]
'mysql'
l[-2]
'fastapi'
l[2]
'c'
l[3]
'flask'
l[4]
'fastapi'
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql']
l[:3]
['python', 'java', 'c']
l[:-3]
['python', 'java', 'c']
l[2:5]
['c', 'flask', 'fastapi']
l[1::2]
['java', 'flask', 'mysql']
l[::2]
['python', 'c', 'fastapi']
l[::-1]
['mysql', 'fastapi', 'flask', 'c', 'java', 'python']
ll[-3:-6:-1]
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    ll[-3:-6:-1]
NameError: name 'll' is not defined. Did you mean: 'l'?
l[-3:-6:-1]
['flask', 'c', 'java']
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql']
'c' in l
True
'mysql' in l
True
'html' not in l
True
'css' in l
False
'''Methods'''
'Methods'
len(l)
6
sorted(l)
['c', 'fastapi', 'flask', 'java', 'mysql', 'python']
max(l)
'python'
min(l)
'c'
l
['python', 'java', 'c', 'flask', 'fastapi', 'mysql']
id(l)
1485343979712
l[3]='css'
l
['python', 'java', 'c', 'css', 'fastapi', 'mysql']
id(l)
1485343979712
l[1] = 'html'
l
['python', 'html', 'c', 'css', 'fastapi', 'mysql']
id(l)
1485343979712
l[2] = 'c++'
l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql']
id(l)
1485343979712
l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql']
a.append('a')
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    a.append('a')
NameError: name 'a' is not defined
l.append('a')
l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'a']
l.append('b')
l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'a', 'b']
l.append('c')
l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'a', 'b', 'c']
id(l)
1485343979712
l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'a', 'b', 'c']
l.extend([1,2,3,4,5])
l
['python', 'html', 'c++', 'css', 'fastapi', 'mysql', 'a', 'b', 'c', 1, 2, 3, 4, 5]
l.insert(1,'flask')
l
['python', 'flask', 'html', 'c++', 'css', 'fastapi', 'mysql', 'a', 'b', 'c', 1, 2, 3, 4, 5]
l.insert(2,'c')
l
['python', 'flask', 'c', 'html', 'c++', 'css', 'fastapi', 'mysql', 'a', 'b', 'c', 1, 2, 3, 4, 5]
id(l)
1485343979712
