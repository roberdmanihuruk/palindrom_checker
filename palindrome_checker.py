# -*- coding: utf-8 -*-
"""palindrome_checker code
Created by:
        Roberd (https://medium.com/@roberdmanihuruk17)

Check if a word is a palindrome or not.
"""

def palindrome_checker (word):
    lowered = word.lower()
    reversed = lowered[::-1]
        
## if else code to check wheater a word is palindrome or not    

    if lowered == reversed:
        print("'" + word + "' is a Palindrome")
    else:
        print("'" + word + "' is NOT a Palindrome")

palindrome_checker('212')

palindrome_checker('098767890')

palindrome_checker('sentences')

palindrome_checker('racecar')
