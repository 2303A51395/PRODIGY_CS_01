def caesar_cipher(text, shift, decrypt=False):
    result = ""
    if decrypt:
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  
    return result
def main():
    while True:
        mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt (or 'exit' to quit): ").strip().lower()
        if mode == 'exit':
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid mode. Please try again.")
            continue
        message = input("Enter your message: ")
        shift = int(input("Enter shift value (1-25): "))
        if shift < 1 or shift > 25:
            print("Shift value must be between 1 and 25.")
            continue
        if mode == 'encrypt':
            encrypted_message = caesar_cipher(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        else:
            decrypted_message = caesar_cipher(message, shift, decrypt=True)
            print(f"Decrypted message: {decrypted_message}")
if __name__ == "__main__":
    main()