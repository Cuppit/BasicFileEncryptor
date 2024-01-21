# Basic File Encryptor
A pair of Python scripts demonstrating simple password based encryption/decryption of files using the PYCA's cryptography library.

## HOW TO USE
Copy the project files to a directory.  In a terminal, `cd` to that directory and run:

  `pip install -r requirements.txt` (This will install the cryptography library if it isn't already available in your environment)

### ENCRYPTING A FILE

You have a few options:

1) `python encrypt.py` (You will be prompted to manually type the filename (or full path to the file) and password to encrypt the file with.)
2) `python encrypt.py <filename>` (you will be prompted only to input the password to encrypt the file with.)
3) `python encrypt.py <filename> <password>` (the script will encrypt the file with the provided password)

### DECRYPTING A FILE

You have a few options:

1) `python decrypt.py` (You will be prompted to manually type the filename (or full path to the file) and password to decrypt the file.)
2) `python decrypt.py <filename>` (you will be prompted only to input the password to decrypt the file with.)
3) `python decrypt.py <filename> <password>` (the script will decrypt the file with the provided password)
