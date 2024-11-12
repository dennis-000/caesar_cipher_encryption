def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        # Check if character is an uppercase letter
        if char.isupper():
            # Shift character within uppercase ASCII range (A-Z)
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        
        # Check if character is a lowercase letter
        elif char.islower():
            # Shift character within lowercase ASCII range (a-z)
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        
        # If character is not a letter, keep it unchanged
        else:
            encrypted_text += char
    
    return encrypted_text

# Take user input for text and shift value
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value: "))

# Encrypt the text and display the result
encrypted_text = caesar_cipher_encrypt(text, shift)
print("Encrypted text:", encrypted_text)
