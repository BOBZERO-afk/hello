import sys
import base64
import glob
import os

def decode_text(encoded):
    # Start with the encoded string as bytes
    b = encoded.encode('utf-8')

    # --- Reverse the 20-layer encoding in exact reverse order ---
    b = base64.b85decode(b)                    # layer 20
    b = base64.decodebytes(b)                  # layer 19 (encodebytes)
    b = base64.b16decode(b)                    # layer 18
    b = base64.b32hexdecode(b)                 # layer 17
    b = base64.z85decode(b)                     # layer 16
    b = base64.b16decode(b)                    # layer 15
    b = base64.standard_b64decode(b)           # layer 14
    b = base64.b16decode(b)                    # layer 13
    b = base64.b85decode(b)                     # layer 12
    b = base64.b16decode(b)                    # layer 11
    b = base64.b32hexdecode(b)                 # layer 10
    b = base64.b16decode(b)                    # layer 9
    b = base64.z85decode(b)                     # layer 8
    b = base64.standard_b64decode(b)           # layer 7
    b = base64.b16decode(b)                    # layer 6
    b = base64.b85decode(b)                     # layer 5
    b = base64.b32hexdecode(b)                 # layer 4
    b = base64.b64decode(b)                     # layer 3
    b = base64.b32decode(b)                     # layer 2
    b = base64.b16decode(b)                     # layer 1
    b = base64.b64decode(b)                     # layer 0 (original b64)

    return b.decode('utf-8')


def decode_from_file():
    files = glob.glob("INFO_TEXT_*.txt")
    if not files:
        print("No INFO_TEXT files found.")
        return

    newest = max(files, key=os.path.getctime)
    with open(newest, "r") as f:
        encoded_text = f.read().strip()

    decoded = decode_text(encoded_text)
    print(f"Decoded from file '{newest}':")
    print(decoded)


def decode_from_argument(arg):
    decoded = decode_text(arg)
    print("Decoded from argument:")
    print(decoded)


# ---------------- MAIN ----------------
if len(sys.argv) < 2:
    print("Usage:")
    print("  python DECODE.py True")
    print("  python DECODE.py <encoded_text> False")
    sys.exit(1)

flag = sys.argv[1].lower() == "true"

if flag:
    decode_from_file()
else:
    if len(sys.argv) < 3:
        print("Error: When using False, you must provide encoded text.")
        sys.exit(1)
    encoded_text = sys.argv[1]
    decode_from_argument(encoded_text)
