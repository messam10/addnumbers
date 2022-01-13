def add(x, y, z = 0):
    return x + y + z

print(add(2, 3)) # output 5
print(add(2, 3, 4)) # output 9

#-------- or -----------------

def add(*x):
    return sum(x)

print(add(2, 3)) # output 5
print(add(2, 3, 4)) # output 9