# Your code here

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
for char in robin:
  if char in charFilter:
    robinFiltered += charFilter[char]
  else: 
    robinFiltered += char

words = robinFiltered.split()
histogram = {}
for word in words:
  if word in histogram:
    histogram[word] += 1
  else:
    histogram[word] = 1
histogramItems = list(histogram.items())
histogramItems.sort(key = lambda t: t[1], reverse = True)
for touple in histogramItems:

  print(f"{touple[0]}{(20 - len(touple[0])) * ' '}{touple[1] * '#'}")