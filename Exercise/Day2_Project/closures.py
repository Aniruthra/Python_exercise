def outer(x):
    def inner(y):
        return x+y
    
    return inner
a=outer(10)

print(a(20))