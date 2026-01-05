import hashlib
import os
import random
from datetime import datetime
from getpass import getpass

_ITERATIONS = 120_000

def _hash_pass(password, salt):
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, _ITERATIONS)
    return dk.hex()

def signup(users):
    """
    ask for username
    check its validity
    ask password and confirm it
    store password securely
    save users as and when in usess.json
    """
    print("\n New User Signup")

    username = input("Enter your username:")
     
    if not username:
        print("'Username cannot be Empty")
        return  
    
    if users.find_user_by_username(username):
        print("Username already taken. Please choose a different username.")
        return 
    
    password = getpass()
    confirm_passwordd = getpass("Confirm password:")

    if not password == confirm_passwordd:
       print("Passwords do not match,Please try again")
       return

    if len(password)<6:     
        print("Password  cannot be less than 6 characters")
        return

    salt = os.urandom(16)
    hashed_password = _hash_pass(password, salt)


    user = {
        "user_id": str(random.random()),
        "username": username,
        "password_hash": hashed_password,
        "salt": salt.hex(),
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    users.add_user(user)
    print("Sign Up Successful! You can now login.")


def login(users):
    print("Login existing user")
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    user = users.find_user_by_username(username)
    if not user:
        print("User not found. Please sign up first.")
        return None
    
    salt = bytes.fromhex(user["salt"])
    entered_hashed_password = _hash_pass(password, salt)

    if entered_hashed_password != user["password_hash"]:
        print("Incorrect password. Please try again.")
        return None
    
    print("Login Successful! Welcome back,", username)
    return user    