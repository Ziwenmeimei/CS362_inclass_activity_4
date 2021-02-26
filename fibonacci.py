def fib(n):
   if n <= 1:
       return n
   else:
       return(fib(n-1) + fib(n-2))

def test_fib_1():
    assert fib(10) == 55

def test_fib_2():
    assert fib(5) == 5

def test_fib_3():
    assert fib(7) == 13

print(fib(10))


def factorial(m):
    if m == 0:
        return 1
    else:
        return m * factorial(m-1)

def test_fac_1():
    assert factorial(4) == 24

def test_fac_2():
    assert factorial(3) == 6

def test_fac_3():
    assert factorial(6) == 720

print(factorial(4))