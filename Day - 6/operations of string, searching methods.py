Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s = 'python'
s
'python'
p = ''
p
''
t = 'programming'
s
'python'
t
'programming'
'''concatination'''
'concatination'
s+t
'pythonprogramming'
'''Repetation'''
'Repetation'
t*3
'programmingprogrammingprogramming'
s * 7
'pythonpythonpythonpythonpythonpythonpython'
'*' * 20
'********************'
'0' * 30
'000000000000000000000000000000'
s = 'python java flask mysql fastapi'
s
'python java flask mysql fastapi'
s[7]
'j'
s[-1]
'i'
s[-4]
't'
s[-7]
'f'
s[12]
'f'
s
'python java flask mysql fastapi'
s[0:6:1]
'python'
s[7:11:1]
'java'
s
'python java flask mysql fastapi'
s[:6]
'python'
s[7:11]
'java'
s[12:17]
'flask'
s[18:23]
'mysql'
s[24:]
'fastapi'
s[::-1]
'ipatsaf lqsym ksalf avaj nohtyp'
s[-7:]
'fastapi'
s[::2]
'pto aafakmslfsai'
s[-15:-20:-1]
'ksalf'
s[5:0:-1]
'nohty'
s[5::-1]
'nohtyp'
'java' in s
True
'mysql' in s
True
'c++' not in s
True
'python' not in s
False
s
'python java flask mysql fastapi'
'''length'''
'length'
len(s)
31
'''Numerical code'''
'Numerical code'
ord('0')
48
ord('1')
49
ord('*')
42
ord('/')
47
ord('a')
97
'''character'''
'character'
chr(22)
'\x16'
chr(10)
'\n'
chr(20)
'\x14'
s
'python java flask mysql fastapi'
'''max'''
'max'
max(s)
'y'
'''min'''
'min'
min(s)
' '
'''sorted'''
'sorted'
sorted(s)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'f', 'f', 'h', 'i', 'j', 'k', 'l', 'l', 'm', 'n', 'o', 'p', 'p', 'q', 's', 's', 's', 't', 't', 'v', 'y', 'y']
s
'python java flask mysql fastapi'
s.upper()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.lower()
'python java flask mysql fastapi'
s.swapcase()
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.title()
'Python Java Flask Mysql Fastapi'
s.capitalize()
'Python java flask mysql fastapi'
s = 'python'
s.center(40,'-')
'-----------------python-----------------'
s.center(40,' ')
'                 python                 '
s.center(40,'*')
'*****************python*****************'
s.ljust(40,'*')
'python**********************************'
s.rjust(40,'*')
'**********************************python'
'1'.zfill(5)
'00001'
'123'.zfill(5)
'00123'
'1234567'.zfill(5)
'1234567'
'''searching methods'''
'searching methods'
s
'python'
s = 'python java flask mysql fastapi'
s
'python java flask mysql fastapi'
s.find('y')
1
s.find('z')
-1
s.find('a')
8
s.rfind('a')
28
s.rfind('t')
27
s.index('z')
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s.index('f')
12
s.count('a')
5
s.count('y)
        
SyntaxError: unterminated string literal (detected at line 1)
s.count('y')
        
2
s.count('z')
        
0
s = '                  code gnan                  '
        
s
        
'                  code gnan                  '
s.strip()
        
'code gnan'
s.lstrip()
        
'code gnan                  '
s.rstrip()
        
'                  code gnan'
s = 'python java flask mysql fastapi'

s
        
'python java flask mysql fastapi'
s.replace('a','*')
        
'python j*v* fl*sk mysql f*st*pi'
s.replace('p','1')
        
'1ython java flask mysql fasta1i'
s
        
'python java flask mysql fastapi'
s.maketrans('apkqs', '12345')
        
{97: 49, 112: 50, 107: 51, 113: 52, 115: 53}
s.translate(s.maketrans('apkqs','12345'))
        
'2ython j1v1 fl153 my54l f15t12i'
s.translate(s.maketrans('aeiou','12345'))
        
'pyth4n j1v1 fl1sk mysql f1st1p3'
