charFilter = {':',';',',','.','-','+','=','/','\\','|','[',']','{','}','(',')','*','^','&','\"'}
def word_count(s):
    # Your code here
    # Make the string all lower
    s = s.casefold()

    # Ignore every character in the string if it's in the
    # characterfilter. Add every other character to filtered string.
    filteredString = ""
    for char in s:
        if char in charFilter:
            continue
        else:
            filteredString += char
    
    # Split the string into a list of words
    wordArr = filteredString.split()
    
    # Add every word to the dictionary. If the word is already in
    # the dictionary increase it's value by one. So the value of
    # the word should be the number of times the word apears.
    wordDict = {}
    for word in wordArr:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1
    return wordDict



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))