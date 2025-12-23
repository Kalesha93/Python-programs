def encrypt(text, shift):
    result = ""
    for ch in text:
        result += chr(ord(ch) + shift)
    return result

def decrypt(text, shift):
    result = ""
    for ch in text:
        result += chr(ord(ch) - shift)
    return result

msg = input("Enter message: ")
s = 3

enc = encrypt(msg, s)
print("Encrypted:", enc)
print("Decrypted:", decrypt(enc, s))
