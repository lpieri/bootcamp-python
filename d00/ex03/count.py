import string
import sys


toPrint = """The text contains {len} characters:

- {upper} upper letters

- {lower} lower letters

- {punc} punctuation marks

- {space} spaces"""


def text_analyzer(s='', *args):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.'''
    if args:
        print("ERROR")
        return
    if not s:
        s = input("What is the text to analyse?\n")
    lenStr = len(s)
    upperCounter = 0
    lowerCounter = 0
    puncCounter = 0
    spaceCounter = 0
    for c in s:
        if c.isupper():
            upperCounter += 1
        elif c.islower():
            lowerCounter += 1
        elif c.isspace():
            spaceCounter += 1
        elif c in str(string.punctuation):
            puncCounter += 1
    printFormat = toPrint.format(
        len=lenStr,
        upper=upperCounter,
        lower=lowerCounter,
        space=spaceCounter,
        punc=puncCounter
        )
    print(printFormat)
