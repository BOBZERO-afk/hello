import base64

def decode_text(encoded_text):
    b1 = encoded_text.encode('utf-8')
    b2 = base64.b16encode(b1)
    b3 = base64.urlsafe_b64encode(b2)
    output = b3.decode('utf-8')
    return output

x = input("Input text: ")
decode_text(x)
print("Decoded text:", decode_text(x))
input("Press Enter to exit...")