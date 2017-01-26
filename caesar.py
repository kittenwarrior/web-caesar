import string

def rotate_character(char, rot):
    charIndex = alphabet_position(char)

    newIndex = (charIndex + rot) % len(string.ascii_lowercase)

    newChar = string.ascii_lowercase[newIndex]

    if char.isupper() == True:
        return newChar.upper()
    else:
        return newChar

def alphabet_position(char):
    lowerAlphabet = ""

    lowerAlphabet = string.ascii_lowercase

    return lowerAlphabet.index(char.lower())

def encrypt(text, rot):

    newString = ""

    for char in text:

        if char.isalpha() == True:
            newString += rotate_character(char, rot)
        else:
            newString += char

    return newString
