fn = lambda z: 'fizzbuzz' if z % 15 == 0 else 'fizz' if z % 3 == 0 else 'buzz' if z % 5 == 0 else z
for y in map(fn, range(1, 101)):
    print y
