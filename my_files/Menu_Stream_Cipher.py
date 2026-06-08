while True:
    print("\n STREAM CIPHER MENU ")
    print("1. Encrypt Message")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        message = input("Enter message: ")
        key = int(input("Enter key (0-255): "))

        encrypted = []

        for char in message:
            encrypted.append(ord(char) ^ key)

        print("\nEncrypted Data:")
        print(encrypted)

        decrypted = ""

        for value in encrypted:
            decrypted += chr(value ^ key)

        print("Decrypted Message:")
        print(decrypted)

    elif choice == "2":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")