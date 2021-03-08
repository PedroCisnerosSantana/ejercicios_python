!#/usr/bin/python3
def factorial(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

factorial(8)

def add(n, *args):
    res = n
    for i in args:
        res += i
    return res

add(1)
add(2,3)

cua = lambda x: x**2
cua(2)
