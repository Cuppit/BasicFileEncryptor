"""
This encrypts the contents of a file using the Fernet library.
A sister script, 'decrypt.py', should have come with this script.

*** WARNING *** FOR EDUCATIONAL PURPOSES ONLY.  DO NOT USE ON 
SENSITIVE DATA.  THIS SOFTWARE COMES WITH ABSOLUTELY NO WARRANTY.  USE AT YOUR OWN RISK.
***************

TECHNICAL NOTE: The encryption key used is a result of a PBKDF2. In order for PBKDF2 to return the same encryption key it must get the exact same parameters. That includes salt, which in this program is generated randomly.

The generated salt will be stored together with the encrypted file in order to be able to decrypt it later  This tip courtesy of Andrew Morozko:

https://stackoverflow.com/questions/55881428/fixing-invalid-signature-when-decrypting-fernet-token

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

if len(sys.argv) > 1:  # If one argument passed, it's presumed to be the path of the file to encrypt.
    # ... use it as path to file to encrypt.
    file = sys.argv[1]
else:
    # ... otherwise, user inputs filename manually.
    file = input('Enter the name of file to encrypt (may need to put absolute path): ')

if len (sys.argv) > 2: #If 2 arguments, the 2nd argument is presumed to be the desired password.
    pw = sys.argv[2]
else:    
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
in_file.close()

password = pw.encode('UTF-8')

salt = os.urandom(16) #It's important to include the salt somehow in the encrypted file.
print("random salt is: ",salt)
print("salt is of type: ",type(salt))
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=480000,
)
key = base64.urlsafe_b64encode(kdf.derive(password))

f = Fernet(key)
token = f.encrypt(data)

out_file = open(file, "wb")
out_file.write(token)
out_file.write(b' ')
out_file.write(salt)
out_file.close()

print("Done.")