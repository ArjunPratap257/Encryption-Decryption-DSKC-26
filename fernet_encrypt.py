from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)

with open("secret.key", "wb") as f:
    f.write(key)
    print("Key saved to secret.key")
    print("Secret Key Is:", key)
    print("b'_' in the secret key means , it's a bytes not a string")

# Normal Text Encryption
message = input("Enter message to encrypt: ")
encrypted_message = fernet.encrypt(message.encode())
print("Encrypted message:", encrypted_message)

with open("secret.key", "rb") as f:
    loaded_key = f.read()
    fernet = Fernet(loaded_key)
    print("Loaded key:", loaded_key)

decrypted_message = fernet.decrypt(encrypted_message).decode()
print("Decrypted message:", decrypted_message)

# Text Encryption from text file
with open("text.txt", "rb") as f:
    sentence = f.read()

encrypted_sentence = fernet.encrypt(sentence)

with open("encrypted_text.txt", "wb") as f:
    f.write(encrypted_sentence)

print("file saved as encryted_text.txt!")

decrypted_sentence = fernet.decrypt(encrypted_sentence)
with open("decrypted_text.txt", "wb") as f:
    f.write(decrypted_sentence)

print("decrypted text saved as decrypted_text.txt!")
print("Original text:", sentence.decode())

# Encrypting of Image
with open("TuffBaby.png", "rb") as f:
    image_data = f.read()

encrypted_image = fernet.encrypt(image_data)

with open("encrypted_TuffBaby.png", "wb") as f:
    f.write(encrypted_image)

print("Image saved as encrypted_TuffBaby.png!")

decrypted_image = fernet.decrypt(encrypted_image)

with open("decrypted_TuffBaby.png", "wb") as f:
    f.write(decrypted_image)

print("decrypted image saved as decrypted_TuffBaby.png!")
