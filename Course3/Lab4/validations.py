#!/usr/bin/env python3

import re

def validate_user(username, minlen):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    
    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
#    if username[0] not in "abcdefqhijklmnopqurstuvwxyz":
#	return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username) or username[0] not in "abcdefqhijklmnopqursuvwxyz":
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True


print(validate_user("blue.kale",3)) #True
print(validate_user(".blue.kale", 3)) #currently true, shoudl be false
print(validate_user("red.quinoa", 4)) #Ture
print(validate_user("_red_quinao", 4)) #currently True, Shoud be False.
