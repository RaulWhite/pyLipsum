from chiquitoDict import chiquitoDict
from random import choice, randint
import logging

logging.basicConfig(format='\n%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def ipsum(dict: classmethod, paragraphs: int, lorem: bool):
    output = "" # Variable declaration
    if lorem: output = dict.start # If start is desired
    for i in range(paragraphs): # Loop for paragraphs
        numPhrases = randint(5, 10)
        for j in range(numPhrases): # Loop for phrases
            numWords = randint(4, 12)
            for k in range(numWords): # Loop for every array item selected
                word = choice(dict.array) # Random array item
                if k == 0 and not (i == j == 0 and lorem):
                    word = word.capitalize() # Capitalize every start of phrase
                if j == 0 and k == 0 and not (i == 0 and lorem):
                    output = output + word # Do not separate by space at start of paragraph
                else:
                    output = output + " " + word
            output = output + "." # Dot every end of phrase
        if paragraphs > 1 and i < (paragraphs - 1):
            output = output + "\n\n" # Separate paragraphs if more than one
    print(output) # Print result

if __name__ == '__main__':
    ipsum(chiquitoDict, 3, True)