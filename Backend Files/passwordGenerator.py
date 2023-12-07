import string
import secrets


def GetaPassword():
    symbols = ['*', '%', '#','$','@'] 
    password = ""
    for _ in range(9):
        password += secrets.choice(string.ascii_lowercase)
    password += secrets.choice(string.ascii_uppercase)
    password += secrets.choice(string.digits)
    password += secrets.choice(symbols)
    return password