x = [1, 2, 3, 4]
y = [7, 6, 4, 5]
z = ['a', 'b', 'c', 'd']

for a,b,c in zip(x,y,z):
    print(a,b,c)

for i in zip(x,y,z):
    print(i)

print(dict(zip(z,y)))

[print(a,b,c) for a,b,c in zip(x,y,z)]


[print(a, b) for a,b in zip(x,y)]
