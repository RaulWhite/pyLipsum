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
        j = 0
        while j < numPhrases:
            numWords = randint(4, 12)
            ### "Word" or array item loop
            k = 0
            while k < numWords:
                ### Check start
                if i == j == 0 and lorem: # At first phrase
                    if start[-1:] == ".":
                        break # If start is a phrase, generate 1 less
                    elif len(start.split()) > numWords:
                        if output[-1:] != ".":
                            output = output + "."
                        break # If start has no period, and has more words than numWords, make it a phrase
                    elif k == 0: # Check words on start, and generate number of words less on first random phrase
                        k += len(start.split())
                ### Random text
                word = choice(dict.array) # Random array item
                if len(word.strip().split()) > 1: # If dictionary item has more than 1 word, generate number less
                    k += (len(word.strip().split()) - 1)
                if word.strip()[-1:] == ".": 
                    k = numWords # If dictionary item is a phrase (has period), generate 1 phrase less
                    if output.strip()[-1:] != "." and output != "":
                        output = output + "." # Punctuate aready generated paragraph output if necessary
                        j += 1 # Count phrase if there was more output generated
                if output.strip()[-1:] == "." or output == "":
                    word = word.capitalize() # Capitalize every start of phrase
                if j < numPhrases: # Check if phrase on item array is generating more phrases than expected
                    if output == "": # Space every word and start of phrase, not start of paragraph
                        output = word
                    else:
                        output = output + " " + word
                k += 1
            ### Punctuation.
            if output.strip()[-1:] != ".":
                output = output + "." # Dot every end of phrase
            ###Phrase loop
            j += 1
        ### Blank lines every paragraph
        if numParags > 1 and i < (numParags - 1):
            output = output + "\n" # Separate paragraphs if more than one
        ### Print paragraph and clear output variable
        print(output)
        output = ""

if __name__ == '__main__':
    ipsum(chiquitoDict, 5, True)