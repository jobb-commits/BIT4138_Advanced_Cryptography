a = 5
c = 3
m = 16
seed = 7

print("LCG Sequence:")

x = seed

for i in range(10):
    x = (a * x + c) % m
    print(x)