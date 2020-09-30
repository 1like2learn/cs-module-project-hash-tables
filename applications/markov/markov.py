import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
wordsArr = words.split()
startWords = []
nextWords = {}
endingPunctuation = {".", "?","!"}
# Loop through all the words in wordsArr
for i,word in enumerate(wordsArr):
    # If the word has an uppercase char add it to the list of start words
    if not word.islower():
        startWords.append(word)
    # If the word is a key in nextWords add the word in the next index to 
    # the word's list of next words
    if word in nextWords:
        nextWords[word].append(wordsArr[i + 1])
    # If the word is not a key make it one and create an array with it's 
    # next word as the only entry
    else:
        # Check to make sure we aren't at the end of the input
        if i + 1 < len(wordsArr):
            nextWords[word] = [wordsArr[i + 1]]

# TODO: construct 5 random sentences
# Your code here
def constructSentence():
    # Our output and current word are randomly taken from startWords
    output = word = random.choice(startWords)
    # Loop while the length of the word is less than one or word is an end word
    while len(word) < 1 or (not word[-1] in endingPunctuation and not word[-2] in endingPunctuation):
        # Make word the next word from nextWords
        word = random.choice(nextWords[word])
        # Add the next word to the output
        output += " " + word
    return output
print(constructSentence())
print(constructSentence())
print(constructSentence())
print(constructSentence())
print(constructSentence())


