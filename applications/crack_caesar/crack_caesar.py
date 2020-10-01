# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
charFilter = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

# Open the provided file
with open("ciphertext.txt") as f:
  words = f.read()

letterCache = {}
# We can calculate the percent of characters each letter is with this
totalNumChar = 0

# If the character is in the filter we increase the total number of 
# characters. Then we check if the character is in the cache. We 
# add an entry if it isn't and increase it's value if it is
for char in words:
  if char in charFilter:
    totalNumChar += 1
    if char in letterCache:
      letterCache[char] += 1
    else:
      letterCache[char] = 1

# For every character in the cache calculate it's frequency and store it.
charFrequency = {}
for key in letterCache:
  charFrequency[key] = letterCache[key] / totalNumChar

# Get a list of touples so we can sort them by their value
charFrequencyList = list(charFrequency.items())
charFrequencyList.sort(key = lambda t: t[1], reverse = True)

decipher = {}
lettersByFrequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# Construct the decipher by setting the most common letter to the 
# first letter in the Letter Frequency list
for i, touple in enumerate(charFrequencyList):
  decipher[touple[0]] = lettersByFrequency[i]

# For every char in the dataset add it to deciphered string. 
# If the char shows up in the decipher return the value instead of the key
decipheredWords = ""
for char in words:
  if char in decipher:
    decipheredWords += decipher[char]
  else:
    decipheredWords += char


print(decipheredWords)