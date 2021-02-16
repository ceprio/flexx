class A():
    var = 1
    
a=A()
print(A.var)
print(a.var)
a.var=2
print(A.var)
print(a.var)
print(a.__class__.var)