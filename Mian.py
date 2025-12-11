import subprocess
import time
import glob
import os

# ------------------- Encode -------------------
text_to_encode = input("Input something to encode: ")

# Run ENCODE.py with the text
subprocess.run(["python", "ENCODE.py", text_to_encode])

# Give ENCODE.py a moment to write the file
time.sleep(1)

# ------------------- Find newest encoded file -------------------
encoded_files = glob.glob("INFO_TEXT_*.txt")
if not encoded_files:
    print("No encoded file found!")
    quit()

newest_file = max(encoded_files, key=os.path.getctime)

# Read the encoded text (optional display)
with open(newest_file, "r") as f:
    encoded_text = f.read().strip()

print("\nEncoded text saved in:", newest_file)
print("Preview (first 200 chars):", encoded_text[:200], "...")  # avoids huge output
print("\nDecoding...")

# ------------------- Decode -------------------
# Use the "True" flag to let DECODE.py read the newest file itself
subprocess.run(["python", "DECODE.py", "True"])

input("\nPress Enter to exit...")
