'''
Method Resolution Order (MRO):
---------------------------------------
In multiple inheritance scenarios, any specific attribute or method will initially be
searched in the current class. If not found in the current class,
then next search continues into parent classes in depth-first left to right order.
Searching in this order is called Method Resolution Order (MRO).

Three principles of MRO:
------------------------------
1. The first principle is to search in own class before going for its super classes.
If class B is inherited from A, it will search B first and then goes to A. B(A)

2. The second principle is, if any class is inherited  several classes,
it searches in the order from left to right in the base classes.
For example, if class C is inherited from A and B, syntactically class C(A, B),
then first it will search in A and then in B.

3. The third principle is that it will not visit any class more than once.
That means a class in the inheritance hierarchy is traversed only once exactly.

Understanding MRO gives you clear idea regarding which classes are being executed
and in which sequence. We have a predefined method to see the sequence of execution
of classes. It is: classname.mro()

Demo 1 for MRO
Method Resolution Order (MRO) in Python

Here,

mro(A)=A, object
mro(B)=B, A, object
mro(C)=C, A, object
mro(D)=D, B, C, A, object
Note: Object is a default super class in python.
'''
# to undrstand mro principle use predefined method:
# classname.mro
class A:
   def m1(self):
       print("m1 from A")
class B(A):
   def m1(self):
       print("m1 from B")
class C(A):
   def m1(self):
       print("m1 from C")
class D(B, C):   # 1 sub , 2 or more super classes
   def m1(self):
       print("m1 from D")

d = D()
d.m1()
print(A.mro())
print(B.mro())  #B(A)
print(C.mro())
print(D.mro())

'''
    A
B      C    
   D


'''

