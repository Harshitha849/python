Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
5&14
4
11&12
8
11|12
15
8|9
9
11^12
7
~11
-12
~90
-91
~17
-18
2<<2
8
2<<3
16
2<<1
4
15>>1
7
a = int(input("Enter a String: "))
Enter a String: Harshi
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a = int(input("Enter a String: "))
ValueError: invalid literal for int() with base 10: 'Harshi'
a = input()

a = input("Enter a String: ")
Enter a String: Harshi
a
'Harshi'
a = input()
678
a
'678'
type(a)
<class 'str'>
a = int(input())
243
a
243
a = int(input("Enter the Interger: "))
Enter the Interger: 12
a
12
a = float(input("Enter the Interger: "))
Enter the Interger: 
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a = float(input("Enter the Interger: "))
ValueError: could not convert string to float: ''

a = int(input("Enter the float: "))
Enter the float: 12.2
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a = int(input("Enter the float: "))
ValueError: invalid literal for int() with base 10: '12.2'
a = float(input("Enter the float: "))
Enter the float: 12.2
a
12.2
a = float(input("Enter the float: "))
Enter the float: 12
a
12.0
a = list(input())
76387687361
a
['7', '6', '3', '8', '7', '6', '8', '7', '3', '6', '1']
'69 34 45 54 64 56 55 78 76'.split(' ')
['69', '34', '45', '54', '64', '56', '55', '78', '76']
a
['7', '6', '3', '8', '7', '6', '8', '7', '3', '6', '1']
a = '69 34 45 54 64 56 55 78 76'.split(' ')
a
['69', '34', '45', '54', '64', '56', '55', '78', '76']
map(int, a)
<map object at 0x0000020077A99570>
list(map, a)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    list(map, a)
TypeError: list expected at most 1 argument, got 2
list(map(int, a))
[69, 34, 45, 54, 64, 56, 55, 78, 76]
a = list(map(int, input().split()))
5 56 654 456 4356 6 56
a
[5, 56, 654, 456, 4356, 6, 56]
a = list(map(float, input().split()))
435
56
56
45
a = list(map(float, input().split()))
5
564
564
a = list(map(float, input().split()))
6 54645 645 6456 456 43 6
a
[6.0, 54645.0, 645.0, 6456.0, 456.0, 43.0, 6.0]
a = tuple(map(float, input().split()))
45 564 45 665456 556 46 46 45
a
(45.0, 564.0, 45.0, 665456.0, 556.0, 46.0, 46.0, 45.0)
a = tuple(map(int, input().split()))
54 5 45 6 46 46 3 46 4 6 46 4 643 
a
(54, 5, 45, 6, 46, 46, 3, 46, 4, 6, 46, 4, 643)
a = set(input().split())
4 453 6465 54345 5345 53 5345
a
{'453', '6465', '4', '5345', '53', '54345'}
a = set(map(int, input().split()))
4 5443 56 46 56 464 56 546 4564

a
{546, 5443, 4, 46, 464, 4564, 56}
a = set(map(float, input().split()))
4 45 46 6 4545 756 75 7 5 7 5755555
a
{4545.0, 5755555.0, 4.0, 5.0, 6.0, 7.0, 75.0, 45.0, 46.0, 756.0}
a,b,c = list(map(int, input().split()))
1 2 3
a
1
b
2
c
3
email, password = input().split()
abc@gmail.com 123436
email
'abc@gmail.com'
password
'123436'
a, b, c = list(map(int, input().split()))
436.645 56.64 5456.564
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    a, b, c = list(map(int, input().split()))
ValueError: invalid literal for int() with base 10: '436.645'
a, b, c = list(map(float, input().split()))
5.546 4.5435 45345.54
a
5.546
b
4.5435
c
45345.54
a = eval(input())
[1,2,3,4]
a
[1, 2, 3, 4]
a = eval(input())

"ddfhisuudhfi"
a
'ddfhisuudhfi'
a = eval(input())
(1,2,3,4)
a
(1, 2, 3, 4)
a = eval(input())
{1,2,3,4}
a
{1, 2, 3, 4}
a = eval(input())
{1:2, 2:3, 3:4}
a
{1: 2, 2: 3, 3: 4}
a = eval(input())
True
a
True
a = eval(input())
2+5j
a
(2+5j)
a = 10
b = 10.2
c = "Codegnan"
a
10
b
10.2
c
'Codegnan'
print(a,b,c)
10 10.2 Codegnan
print("a=", a, "b=", b, "c=", c)
a= 10 b= 10.2 c= Codegnan
print("a=", a, "b=", b, "c=", c, sep='')
a=10b=10.2c=Codegnan
print("a=", a, "b=", b, "c=", c, sep='-')
a=-10-b=-10.2-c=-Codegnan
print("a=", a, "b=", b, "c=", c, end='\n\n')
a= 10 b= 10.2 c= Codegnan

print("a=", a, "b=", b, "c=", c, end='@')
a= 10 b= 10.2 c= Codegnan@
print(f'a={a} b={b} c={c}')
a=10 b=10.2 c=Codegnan
print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=10.200000 c=Codegnan
print('a=%d b=%.2f c=%s'%(a,b,c))
a=10 b=10.20 c=Codegnan
print('a={} b={} c={}'.format(a,b,c))
a=10 b=10.2 c=Codegnan
print('a={} b={} c={}'.format(b,c,a))
a=10.2 b=Codegnan c=10
