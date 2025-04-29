from functools import partial

def _xx(a1, a2):
    return a1 + a2

yy = partial(_xx, a2=100)

data = yy(2)
print(data)
