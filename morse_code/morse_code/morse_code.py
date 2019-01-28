#!/usr/bin/env python3

############################################
# Code borrowed and heavily modified from Geeks for Geeks
# https://www.geeksforgeeks.org/morse-code-translator-python/
#
# Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)
# https://creativecommons.org/licenses/by-sa/4.0/
############################################

# Dictionary representing the morse code chart
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# Function to encrypt the string
# according to the morse code chart
def encrypt(message):
    message = message.upper()
    cipher = ''
    for word in message.split(' '):
        for letter in word:
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            try:
                cipher += MORSE_CODE_DICT[letter] + '1'
            except KeyError:
                pass
        cipher[-1] = '7'

    return cipher[:-1]


# Hard-coded driver function to run the program
def main():
    message = "GEEKS-FOR-GEEKS"
    result = encrypt(message.upper())
    print(result)


# Executes the main function
if __name__ == '__main__':
    main()
