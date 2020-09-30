# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# charFilter = {':',';',',','.','-','+','=','/','\\','|','[',']','{','}','(',')','*','^','&','\"'}
charFilter = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'}

with open("ciphertext.txt") as f:
  words = f.read()

letterCache = {}
totalNumChar = 0

for char in words:
  if char in charFilter:
    totalNumChar += 1
    if char in letterCache:
      letterCache[char] += 1
    else:
      letterCache[char] = 1

charFrequency = {}
for key in letterCache:
  charFrequency[key] = letterCache[key] / totalNumChar

charFrequencyList = list(charFrequency.items())
charFrequencyList.sort(key = lambda t: t[1], reverse = True)

decipher = {}
lettersByFrequency = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
print(lettersByFrequency)
print(charFrequencyList)
for i, touple in enumerate(charFrequencyList):
  decipher[touple[0]] = lettersByFrequency[i]
print(decipher)

decipheredWords = ""
for char in words:
  if char in decipher:
    decipheredWords += decipher[char]
  else:
    decipheredWords += char


print(decipheredWords)