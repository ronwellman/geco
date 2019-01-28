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


# Function to encode the string
# according to the morse code chart
def encode(message):
    message = message.upper()
    ciphertext = []
    for word in message.split(' '):
        cipher = ''
        for letter in word:
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            try:
                cipher += MORSE_CODE_DICT[letter] + '1'
            except KeyError:
                pass
        ciphertext.append(cipher.rstrip('1'))

    return '7'.join(ciphertext)


# Hard-coded driver function to run the program
def main():
    message = "GEEKS-FOR-GEEKS"
    result = encode(message.upper())
    print(result)


# Executes the main function
if __name__ == '__main__':
    main()
