state = [1, 0, 1, 1]

print("Initial State:", state)

for i in range(20):
    feedback = state[0] ^ state[3]
    output = state[-1]

    print(output, end=" ")

    state = [feedback] + state[:-1]