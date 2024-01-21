"""
This decrypts the contents of a file using the Fernet library.

*** WARNING *** FOR EDUCATIONAL PURPOSES ONLY.  DO NOT USE ON 
SENSITIVE DATA.  THIS SOFTWARE COMES WITH ABSOLUTELY NO WARRANTY.  USE AT YOUR OWN RISK.
***************

"""
 
 
# NOTE: to encode a string such as in this example, use the encode('UTF-8') method.  
# Example: "hello".encode('UTF-8')
# will yield the bytes value of :    b"hello"
import sys
import base64
import os
from getpass import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

if len(sys.argv) > 1:  #if there was at least one argument passed:
    # ... use it as path to file to encrypt.
    file = sys.argv[1]
else:
    # ... otherwise let the user input the path.
    file = input('Enter the name of file to encrypt (may need to put absolute path): ')

if len (sys.argv) > 2: #if there was at least two arguments passed:
    # ... use the second arg as the password for encryption.
    pw = sys.argv[2]
else:    
    # ... Otherwise, ensure 
    pw = ''
    pw2 = '"'
    while pw != pw2:
        pw = getpass("Enter a password: ")
        pw2 = getpass("Enter the password again: ")
        if pw != pw2: 
            print("The passwords don't match.")

# Reading the file's contents into memory.
in_file = open(file, "rb")
data = in_file.read()
print("in program, variable 'data' is of type: ",type(data))
in_file.close()

#print("here's what the data looks like printed:", data)

password = pw.encode('UTF-8')

if len(data.split(b' ')) < 2:
    print("ERROR: No salt detected.  Was this file encrypted with the 'encrypt.py' tool that came with this script?")
    exit()

salt = data.split(b' ')[1]
data = data.split(b' ')[0]
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))

f = Fernet(key)
decrypted = f.decrypt(data)
print("Done.")

out_file = open(file, "wb")
out_file.write(decrypted)
out_file.close()