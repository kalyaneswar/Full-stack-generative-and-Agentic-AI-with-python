class A:
    label = "A: base class"

class B(A):
    label = "B: Masala Blend"

class C(A):
    label = "C: Herbal blend"

class D (B, C):
    pass

cup = D
print(cup.label)
print(cup.__mro__)