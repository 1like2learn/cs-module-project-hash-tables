def no_dups(s):
    # Your code here
    cache = {}
    stringArr = s.split()
    for word in stringArr:
        if word in cache:
            continue
        else:
            cache[word] = ""
    returnString = ""
    for i,word in enumerate(cache.keys()):
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