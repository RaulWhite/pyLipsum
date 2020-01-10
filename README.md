
# pyLipsum

## Yet another Lorem ipsum generator in python 3... **with dictionaries!**

Yes indeed, this Lorem ipsum generator accepts an array of words, or prewritten phrases for generating random text. It also accepts an start phrase.

### Main program

The main program is in `main.py`, and the main process is `ipsum`.

#### Generation options

`ipsum` takes 3 variables:

|Variable|Type|Description|
|--|--|--|
|`dict`|**classMethod**|The dictionary with start string and an array of strings|
|`numParags`|**int**|Number of paragraphs to be generated|
|`lorem`|**bool**|If the start string shall be written to the random text or not|

#### Dictionaries

The dictionaries are simple classes, with an string `start` and an array `array`. This class passes via the `dict` variable in the `ipsum` method.

In this repository there are examples of dictionaries in the folder [`pyLipsum/dicts`](pyLipsum/dicts)

### Why

Why not?
At the moment this is a basic program that outputs text, but the intention is to make an online generator with a selection page and API.
