s="coronavirus"
s[0]
'c'
s[8]
'r'
s='Hello'
s[0]
'H'
s[4]
'o'
s[5]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s[5]
IndexError: string index out of range
s[:]
'Hello'
s[2:8]
'llo'
s[:4]
'Hell'
s[2:]
'llo'
s[::2]
'Hlo'
s[::-1]
'olleH'
s[-1]
'o'
s[-2]
'l'
s[-3]
'l'
s[-4]
'e'
s[-5]
'H'
s[-6]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    s[-6]
IndexError: string index out of range
s[-5:-1]
'Hell'
s[-4:]
'ello'
s[-5:-2]
'Hel'
s[-5:4]
'Hell'
s[1:-1]
'ell'
s[-5:-1]
'Hell'
s[-5:-1:-1]
''
s[-1:-5:-1]
'olle'
\
[-1:-5:-2]
SyntaxError: invalid syntax
s[-1:-5:-2]
'ol'
s[::-2]
'olH'
