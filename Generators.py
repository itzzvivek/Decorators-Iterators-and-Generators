def multiple_generator(x, n):
    for i in range(1, n + 1):
        yield x * i

multiple_of_5 = multiple_generator(5,3)
print(next(multiple_of_5))
print(next(multiple_of_5))
print(next(multiple_of_5))
