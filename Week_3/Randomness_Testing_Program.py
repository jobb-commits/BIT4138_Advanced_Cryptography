import random

def generate_bits(n):
    return [random.randint(0, 1) for _ in range(n)]

def frequency_test(bits):
    zeros = bits.count(0)
    ones = bits.count(1)
    total = len(bits)

    print("\n--- Frequency Test ---")
    print("Zeros:", zeros)
    print("Ones:", ones)
    print("Balance:", ones / total)

def runs_test(bits):
    runs = 1

    for i in range(1, len(bits)):
        if bits[i] != bits[i - 1]:
            runs += 1

    print("\n--- Runs Test ---")
    print("Number of Runs:", runs)

def mean_test(bits):
    mean = sum(bits) / len(bits)

    print("\n--- Mean Test ---")
    print("Mean Value:", mean)

def save_to_file(bits):
    with open("random_bits.txt", "w") as f:
        f.write("".join(map(str, bits)))
    print("\nBits saved to random_bits.txt")

def analyze(bits):
    print("\nGenerated Bits:")
    print("".join(map(str, bits)))

    frequency_test(bits)
    runs_test(bits)
    mean_test(bits)

def main():
    while True:
        print("\nRANDOMNESS TEST MENU")
        print("1. Generate Random Bits")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            n = int(input("Enter number of bits (100+ recommended): "))
            bits = generate_bits(n)

            analyze(bits)

            save = input("\nSave to file? (y/n): ")
            if save.lower() == "y":
                save_to_file(bits)

        elif choice == "2":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")


main()