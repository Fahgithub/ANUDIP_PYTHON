Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> a=1
>>> b=1.5
>>> c="FARHEEN"
>>> d=5+6j
>>> e={"Dad","Mom","sibling","cousin"}
>>> f=["Sefali",3,4.5,4+5j]
>>> g=True
>>> h=("Darvin",4)
>>> print(type(a))
<class 'int'>
>>> print(type(b))
<class 'float'>
>>> print(type(c))
<class 'str'>
>>> print(type(d))
<class 'complex'>
>>> print(type(e))
<class 'set'>
>>> print(type(f))
<class 'list'>
>>> print(type(g))
<class 'bool'>
>>> print(type(h))
<class 'tuple'>
>>> i={'Daisy':'name','Laura':4,'Aisha':4.5,'Fahh':'cool'}
>>> print(type(i))
<class 'dict'>
>>> import sys
>>> print(f"the size of a is {sys.getsizeof(a)}bytes)
...       
SyntaxError: incomplete input
>>> print(f"the size of a is {sys.getsizeof(a)}bytes")
...       
the size of a is 28bytes
>>> print(f"the size of a is {sys.getsizeof(b)}bytes)
      
SyntaxError: incomplete input
print(f"the size of a is {sys.getsizeof(a)}bytes")
      
the size of a is 28bytes
print(f"the size of a is {sys.getsizeof(a)}bytes")
      
the size of a is 28bytes
print(f"the size of a is {sys.getsizeof(b)}bytes")
      
the size of a is 24bytes
print(f"the size of a is {sys.getsizeof(c)}bytes")
      
the size of a is 56bytes
print(f"the size of a is {sys.getsizeof(d)}bytes")
      
the size of a is 32bytes
print(f"the size of a is {sys.getsizeof(e)}bytes")
      
the size of a is 216bytes
print(f"the size of a is {sys.getsizeof(f)}bytes")
      
the size of a is 88bytes
print(f"the size of a is {sys.getsizeof(g)}bytes")
      
the size of a is 28bytes
print(f"the size of a is {sys.getsizeof(h)}bytes")
      
the size of a is 56bytes
print(f"the size of a is {sys.getsizeof(i)}bytes")
      
the size of a is 184bytes
#boolean type
      
a=true
      
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
a=True
      
b=False
      
print(f"the size of a is {sys.getsizeof(a)}bytes")
      
the size of a is 28bytes
print(f"the size of a is {sys.getsizeof(b)}bytes")
      
the size of a is 28bytes
print(type(a))
      
<class 'bool'>
print(type(b))
      
<class 'bool'>
a=5+3j
      
b=25+45j
      
print(a.real)
      
5.0
print(b.imag)
      
45.0
