a = 5
c = 3
m = 16
x = 7  # seed

print("LCG Sequence:")

for i in range(20):
    x = (a * x + c) % m
    print(x, end=" ")