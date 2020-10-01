# Your code here
# dictionary that will help filter out symbols and replace caps with lower
charFilter = {
    ':': '',
    ';': '',
    ',': '',
    '.': '',
    '-': '',
    '+': '',
    '=': '',
    '/': '',
    '\\': '',
    '|': '',
    '[': '',
    ']': '',
    '{': '',
    '}': '',
    '(': '',
    ')': '',
    '*': '',
    '^': '',
    '&': '',
    '\"': '',
    'A': 'a',
    'B': 'b',
    'C': 'c',
    'D': 'd',
    'E': 'e',
    'F': 'f',
    'G': 'g',
    'H': 'h',
    'I': 'i',
    'J': 'j',
    'K': 'k',
    'L': 'l',
    'M': 'm',
    'N': 'n',
    'O': 'o',
    'P': 'p',
    'Q': 'q',
    'R': 'e',
    'S': 's',
    'T': 't',
    'U': 'u',
    'V': 'v',
    'W': 'w',
    'X': 'x',
    'Y': 'y',
    'Z': 'z'
}


with open("robin.txt") as f:
  robin = f.read()

robinFiltered = ""
# Add all desired characters to robinFiltered from the provided data
for char in robin:
  if char in charFilter:
    robinFiltered += charFilter[char]
  else: 
    robinFiltered += char

# Create a list of words from robinFiltered
words = robinFiltered.split()
histogram = {}

# Add every unique word to the histogram dictionary and increase the value per duplicate
for word in words:
  if word in histogram:
    histogram[word] += 1
  else:
    histogram[word] = 1
  
# Get a list of touples that coincides to histogram's key value pairs
listHistogramItems = list(histogram.items())
listHistogramItems.sort(key = lambda t: t[1], reverse = True)

# Print the sorted list where every hashmark represents an instance of a 
# word and it's properly formated
for touple in listHistogramItems:
  print(f"{touple[0]}{(20 - len(touple[0])) * ' '}{touple[1] * '#'}")