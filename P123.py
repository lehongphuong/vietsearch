import re

# *******************
# P1 convert string
# *******************
def convertString(line):
    # Define common articles
    common_articles = [' a ',' an ',' the ',' on ',' in '] 

    # Remove special character
    line = ' '.join(re.sub('[^a-zA-Z ]', '', line).strip().split())

    # Remove common articles from string
    for item in common_articles:
        line = re.sub(item,' ',line)  

    # Sort the words in alphabetical order    
    list_works = line.split(' ')
    list_works.sort(key=lambda x:x.split()[-1])
    
    return ' '.join(list_works)

line = 'I like   to  	Program the a  on in  in Python Language. Don’t you?   1   '
line1 = 'don i language like program python  t you' 

print(convertString('I like   to  	Program   in Python Language. Don’t you?'))


# *******************
# P2 Unit test for method convert string
# *******************
def assertP2(input1, ouput1):
    print(convertString(input1) == ouput1)
    
# testcase 1: Do not contain separator like ,./”:|;\-[]()?. …
input1 = 'love !@@#$%#$^%^&^$*()<>?:;/][[]]'
ouput1 = 'love'
assertP2(input1,ouput1)

# testcase 2: Accept only single space, digit or alphabetic word.
input1 = 'love !@@#$%#$^%^&^$*()<>?:;/][[]] you'
ouput1 = 'love you'
assertP2(input1,ouput1)

# testcase 3: Do not contain any common articles like “a”, “the”, “on”, “in”…
input1 = 'a love is the happy on people and in the world!'
ouput1 = 'a and happy is love people world'
assertP2(input1,ouput1)

# testcase 4: a and happy is love people world
input1 = 'work you i a lone love him'
ouput1 = 'him i lone love work you'
assertP2(input1,ouput1)

# testcase 5: full test
input1 = 'I like   to  	Program   in Python Language. Don’t you?' 
ouput1 = 'Dont I Language Program Python like to you'
assertP2(input1,ouput1)


import nltk 
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
# nltk.download('punkt') # donwload model punkt one time

# *******************
# P3 Generater Unigrams, Bigrams, Trigrams from output P1
# *******************
def generateUniBiTri(word):
    # tokenize word
    token = word_tokenize(word)
    
    # generate ngrams
    unigrams = ngrams(token,1)
    bigrams = ngrams(token,2)
    trigrams = ngrams(token,3) 
    
    return [unigrams, bigrams, trigrams]


# Test P3 funtion
input1 = 'I like   to  	Program   in Python Language. Don’t you?' 
text = convertString(input1)
ouput_generate = generateUniBiTri(text)

print(Counter(ouput_generate[0]))
print(Counter(ouput_generate[1]))
print(Counter(ouput_generate[2]))