for y in [('fizzbuzz' if x % 15 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else x) for x in range(1,101)]:
    print y
