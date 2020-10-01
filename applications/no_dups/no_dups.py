def no_dups(s):
    # Your code here
    cache = set()
    # Get a list of words in the string
    stringArr = s.split()

    # If the word is in the set ignore it. Otherwise add it to the cache
    for word in stringArr:
        if word in cache:
            continue
        else:
            cache.add(word)
    
    # Add every word to the return string with a space before it if it's not the first word
    returnString = ""
    for i,word in enumerate(cache):
        if i == 0:
            returnString += word
        else:
            returnString += " " + word
    return returnString



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))