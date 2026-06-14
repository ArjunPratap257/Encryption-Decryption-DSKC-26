import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

img = Image.open("TuffBaby.png")
img_array = np.array(img)

key = 67
encrypted = img_array ^ key
decrypted = encrypted ^ key

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(img_array)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(encrypted)
plt.title("Encrypted Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(decrypted)
plt.title("Decrypted Image")
plt.axis("off")

plt.suptitle("XOR Image Encryption — DSKC-26", fontsize=14)
plt.tight_layout()

print("""
XOR Method Explaination.
ASCII Value of 'H' = 72
H alphabet in binary: 1 0 0 1 0 0 0
67 in binary: 0 1 0 0 0 1 0 1
"^" in the code means XOR (exclusive OR)

Original:  1 0 1 1 0 1 0 0  (the letter 'H' = 72)
Key:       0 1 0 0 0 0 1 1  (67)
           ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
Encrypted: 0 0 1 0 1 1 1 0  (= 9, unreadable)

Encrypted: 0 0 1 0 1 1 1 0  (9)
Key:       0 1 0 0 0 0 1 1  (67)
           ↓ ↓ ↓ ↓ ↓ ↓ ↓
Original:  1 0 1 1 0 1 0 0  (72 = 'H' again!)
""")

plt.show()
