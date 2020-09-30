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
for i,word in enumerate(wordsArr):
    if not word.islower():
        startWords.append(word)
    if word in nextWords:
        nextWords[word].append(wordsArr[i + 1])
    else:
        if i + 1 < len(wordsArr):
            nextWords[word] = [wordsArr[i + 1]]

# TODO: construct 5 random sentences
# Your code here
def constructSentence():
    output = word = random.choice(startWords)
    while len(word) < 1 or (not word[-1] in endingPunctuation and not word[-2] in endingPunctuation):
        word = random.choice(nextWords[word])
        output += " " + word
    return output
print(constructSentence())
print(constructSentence())
print(constructSentence())
print(constructSentence())
print(constructSentence())


