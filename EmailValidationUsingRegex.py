'''
Here, we can see how to use regex - module in python to match any particular pattern
Regex Module- A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
                RegEx can be used to check if a string contains the specified search pattern.
Ex: If we don't know the exact text/string/numbers or any thing to be searched, then we can use 'Regular Expressions' to search for a matching pattern
This module provides different set of functions, metacharacters([],/,^,$,?,+), sets([]),special sequences to create the search pattern.

An email can have the following conditions:
1. small characters (a-z)
2. digits (0-9)
3. before "@", we can have ( '.' or '_' ) - 1 time
4. '@' - symbol 1 time
5. '.' - should be present at 2, 3 position from last.

'''
# '^' -> defines startswith()
# '[]' -> defines range of characters
# '+' -> used to join different expression/condition within a search pattern
# '\' -> defines a special sequence
# '?' -> 0 or 1 occurence exactly.(At a time, we can have only 1 occurence between '.,_' if >1 occurence then the condition becomes false)
# '[\._]?[a-z 0-9]' -> says that only one occurence can be present between '.','_' followed by any character between a-z and 0-9.
# '\w' -> Returns a match where the string contains any word characters (here, looking for '@','.')
# '{}' -> to search at a specified position
# '$' -> defines endswith()

'''
we make use of re.search() from regex module to search and match the pattern.
'''
import re

email_search_pattern = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

user_email = input("Enter email to be checked: ")

if re.search(email_search_pattern, user_email):
    print("Valid Email :) ")
else:
    print("Invalid Email :(")