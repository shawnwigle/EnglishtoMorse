# This is a morse code translator
# import regular expressions for special character checking/substitution
import re


def convert():
    # ask user what message the user wants converted
    message = input("Type a message to be converted: \n")

    # initialize dictionary with english to morse translations
    emdict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
}

    # remove special characters and spaces
    cleanmessage = re.sub('[^A-Za-z0-9]+', '', message)

    # convert to lower case and split into new table containing all letters of message for conversion
    temp = []
    for i in cleanmessage:
        temp.append(i.lower())

    # translate individual english characters to morse and append to new variable
    translated = []
    for i in temp:
        translated.append(emdict[i])

    # convert list of morse characters to string separating each character with a space
    morsemessage = " ".join(translated)

    # output morse message to user
    print("Your message in morse is " + morsemessage)

convert()