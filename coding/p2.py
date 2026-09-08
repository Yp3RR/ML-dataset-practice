def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()

for number in fib:
    print(number)
    if number > 50:  # You decide when to stop
        break