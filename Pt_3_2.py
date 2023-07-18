fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1

for i in range(20):
    print(fib(i))
