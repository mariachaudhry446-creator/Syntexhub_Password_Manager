## Password Manager
A local password manager that stores credentials encrypted on disk using AES symmetric encryption.
## Features
-  Master password protection
-  Add, retrieve, delete, and search passwords
-  AES encryption using Fernet (cryptography library)
-  Encrypted JSON storage format
## How to Run
   pip install cryptography
## Run the program:
   python password_manager.py
## Default Master Password:
    admin123
## Files Generated
  secret.key - Your encryption key 
  vault.json - Encrypted password storage
