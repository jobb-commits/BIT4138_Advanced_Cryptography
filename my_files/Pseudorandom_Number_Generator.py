# Pseudorandom Number Generator 

seed = int(input("Enter seed value: "))

a = 5      # multiplier
c = 3      # increment
m = 16     # modulus

x = seed

print("\nGenerated Sequence:")

for i in range(20):
    x = (a * x + c) % m
    print(f"Value {i+1}: {x}")

print("""
      The generated sequence appears random initially but eventually repeats. The number of values generated before repetition is called the period. In this experiment, the sequence repeated after cycling through the available values determined by the modulus. Larger modulus values generally improve randomness and increase the period length.
""")