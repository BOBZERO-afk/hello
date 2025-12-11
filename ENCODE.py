import base64
import time
import sys

def encode_text(text):
    bob1 = base64.b64encode(text.encode('utf-8'))
    encode_bytes1 = base64.b16encode(bob1)
    encode_bytes2 = base64.b32encode(encode_bytes1)
    encode_bytes3 = base64.b64encode(encode_bytes2)
    encode_bytes4 = base64.b32hexencode(encode_bytes3)
    encode_bytes5 = base64.b85encode(encode_bytes4)
    encode_bytes6 = base64.b16encode(encode_bytes5)
    encode_bytes7 = base64.standard_b64encode(encode_bytes6)
    encode_bytes8 = base64.z85encode(encode_bytes7)
    encode_bytes9 = base64.b16encode(encode_bytes8)
    encode_bytes10 = base64.b32hexencode(encode_bytes9)
    encode_bytes11 = base64.b16encode(encode_bytes10)
    encode_bytes12 = base64.b85encode(encode_bytes11)
    encode_bytes13 = base64.b16encode(encode_bytes12)
    encode_bytes14 = base64.standard_b64encode(encode_bytes13)
    encode_bytes15 = base64.b16encode(encode_bytes14)
    encode_bytes16 = base64.z85encode(encode_bytes15)
    encode_bytes17 = base64.b32hexencode(encode_bytes16)
    encode_bytes18 = base64.b16encode(encode_bytes17)
    encode_bytes19 = base64.encodebytes(encode_bytes18)
    encode_bytes20 = base64.b85encode(encode_bytes19)
    encoded_str = encode_bytes20.decode('utf-8')
    print(f"Encoded text: {encoded_str}")

    filename = f"INFO_TEXT_{int(time.time())}.txt"
    with open(filename, "w") as f:
        f.write(encoded_str)
    print(f"Saved to: {filename}")

if len(sys.argv) > 1:
    text = sys.argv[1]
    encode_text(text)
else:
    print("No argument given!")
    input("")
    sys.exit(1)