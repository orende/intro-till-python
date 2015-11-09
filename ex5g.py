def printFunc(x): print x
fn = lambda z: printFunc('fizzbuzz') if z % 15 == 0 else printFunc('fizz') if z % 3 == 0 else printFunc('buzz') if z % 5 == 0 else printFunc(z)
map(fn, range(1, 101))
