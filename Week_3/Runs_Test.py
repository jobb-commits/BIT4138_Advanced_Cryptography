sequence = "11010010101100101010"

runs = 1

for i in range(1, len(sequence)):
    if sequence[i] != sequence[i - 1]:
        runs += 1

print("Runs Test Result")
print("Sequence:", sequence)
print("Number of Runs:", runs)