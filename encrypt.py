import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)

key = chars.copy()
random.shuffle(key)

print("Basic Text Encryption - DSKC-26")
# print(f"Key: {key}")

plain_text = input("Enter Message To Encrypt: ")
cypher_text = ""
for words in plain_text:
    index = chars.index(words)
    cypher_text += key[index]
print(f"Encrypted Message: {cypher_text}")

cypher_text = input("Enter Message To Decrypt: ")
plain_text = ""
for words in cypher_text:
    index = key.index(words)
    plain_text += chars[index]
print(f"Decrypted Message: {plain_text}")
