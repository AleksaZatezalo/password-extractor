# Chrome Password Extractor
This Python script extracts and decrypts saved passwords from Google Chrome on Windows systems. It works by accessing Chrome's encrypted login database and decrypting it using the system-stored encryption key.

## How it works

The Chrome Password Extractor works using the following 6 steps:

1. Fetch Chrome’s encrypted key from the Local State file.
2. Decrypt the key using Windows DPAPI.
3. Copy Chrome's login database to avoid file-locking issues.
4. Extract login credentials from the database.
5. Decrypt passwords using AES with the previously extracted key.
6. Print the results (including URLs, usernames, passwords, and timestamps).

## Requirements

Ensure you have Python 3.x installed. You also need the following packages:

1. pycryptodome
2. pypiwin32

## Security Notice

This script accesses sensitive personal data. Please use it only on your own machine or with explicit permission from the device owner.