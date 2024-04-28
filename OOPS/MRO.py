'''class A:
    def rk(self):
        print("Class A")
class B(A):
    def rk(self):
        print("Class B")
class C(A):
    def rk(self):
        print("Class C")
class D(C,B):
    pass
r = D()
r.rk()
'''
# mro tells us the order of executing of a method
class A:
    def method(self):
        print("A.method() called")
class B(A):
    def method(self):
        print("B.method() called")
b = B()
b.method()
print(B.mro())
print(B.__mro__)
