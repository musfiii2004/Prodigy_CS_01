def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char.lower()) - 97 + shift_amount) % 26 + 97)
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (q to quit): ").lower()
        if choice == 'q':
            break

        if choice in ['e', 'd']:
            message = input("Enter your message: ")
            shift = int(input("Enter shift value: "))

            if choice == 'e':
                encrypted_message = encrypt(message, shift)
                print(f"Encrypted message: {encrypted_message}")
            elif choice == 'd':
                decrypted_message = decrypt(message, shift)
                print(f"Decrypted message: {decrypted_message}")
        else:
            print("Invalid choice. Please enter 'e', 'd', or 'q'.")

if __name__ == "__main__":
    main()
