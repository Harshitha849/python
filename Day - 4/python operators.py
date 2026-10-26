Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a = 20
b = 10
a +b
30
a-b
10
a*b
200
a/b
2.0
9/2
4.5
a//b
2
9//2
4
9%2
1
a%b
0
2**4
16
7**2
49
3**3
27
''' Comparison operators'''
' Comparison operators'
a
20
b
10
a<b
False
a>
SyntaxError: invalid syntax
a>b
True
a<=b
False
a>=b
True
a==b
False
a!=b
True
'''Assignment operator'''
'Assignment operator'
c = 20
c = c + 10
c
30
c = c-10
c
20
c = c*5
c
100
c += 10
c
110
c -= 10
c
100
c *= 10
c
1000
c /= 10
c
100.0
c //= 10
c
10.0
c %= 10
c
0.0
c *= 2
c
0.0
'''logical operators'''
'logical operators'
a
20
a%2 == 0 and a>10
True
b
10
b%2 == 0 and b>10
False
a%2 == 0 or a>10
True
b%2 == 0 or b>10
True
b%2 == 0
True
not b%2 == 0
False
'''Membership operator'''
'Membership operator'
s = "python"
'p' in s
True
'o' in s
True
'n' in s
True
'z' in s
False
'b' in s
False
'b' not in s
True
'y' not in s
False
l = ["python", "c", "java", "html", "flask"]
"java" in l
True
"html" in l
True
"mysql" in l
False
"java" not in l
False
s = {1,2,3,4,5}
4 in s
True
5 in s
True
6 in s
False
2 not in s
False
d = {1:2, 2:4, 3:6, 4:8, 5:10}
10 in d
False
5 in d
True
4 in d
True
6 in d
False
'''Idenity operator'''
'Idenity operator'
l = [1,2,3,4,5]
m = [1,2,3,4,5]
l == m
True
l is m
False
n = m
n
[1, 2, 3, 4, 5]
id(n)
1480434403520
n is m
True
n is not m
False
n is not l
True
