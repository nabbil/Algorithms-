'''
Checks to see if the word is a palidrome
'''

example = ["racecar", ""]


def check_palindrome(word):
    backward = word[::-1]
    print(backward)
    if backward == example:
        print("This is a Palidrome!!")
    else:
        print("Not a Palidrome")


check_palindrome("civic")

