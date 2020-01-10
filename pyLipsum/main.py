from random import choice, randint
import logging

# Import dictionaries
from dicts.chiquitoDict import chiquitoDict
from dicts.ipsumDict import ipsumDict

logging.basicConfig(format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def ipsum(dict: classmethod, numParags: int, lorem: bool):
    ### Start
    output = "" # Variable declaration
    if lorem:
        output = start = dict.start.strip() # Trim spaces on start
    ### Paragraph loop
    for i in range(numParags):
        numPhrases = randint(5, 10)
        ### Phrase loop
        for j in range(numPhrases):
            numWords = randint(4, 12)
            ### "Word" or array item loop
            for k in range(numWords):
                ### Check start
                if i == j == 0 and lorem: # At first phrase
                    if start[-1:] == ".":
                        break # If start is a phrase, generate 1 less
                    elif len(start.split()) > numWords:
                        if output[-1:] != ".":
                            output = output + "."
                        break # If start is has no period, and has more words than numWords, make it a phrase
                ### Random text
                word = choice(dict.array) # Random array item
                if k == 0 and not (i == j == 0 and lorem and not start[-1:] == "."):
                    word = word.capitalize() # Capitalize every start of phrase
                if j == k == 0 and not (i == 0 and lorem):
                    output = output + word # Do not separate by space at start of paragraph
                else:
                    output = output + " " + word
            ### Punctuation.
            if output[-1:] != ".":
                output = output + "." # Dot every end of phrase
        ### Blank lines every paragraph
        if numParags > 1 and i < (numParags - 1):
            output = output + "\n\n" # Separate paragraphs if more than one
    ### Result
    print(output) # Print result

if __name__ == '__main__':
    ipsum(ipsumDict, 2, True)