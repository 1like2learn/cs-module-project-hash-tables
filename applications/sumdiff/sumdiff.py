"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
functionResults = {}
for num in q:
    functionResults[num] = f(num)
    
addedResults = {}
for num in q:
    for num2 in q:
        addedResults[f'f({num}) + f({num2})'] = functionResults[num] + functionResults[num2]

subbedResults = {}
for num in q:
    for num2 in q:
        result = functionResults[num] - functionResults[num2]
        if result:
            subbedResults[f'f({num2}) - f({num})'] = result
    for num3 in q:
        result = functionResults[num3] - functionResults[num]
        if result:
            subbedResults[f'f({num3}) - f({num})'] = result

addedItems = list(addedResults.items())
subbedItems = list(subbedResults.items())

subbedValues = {}
for item in subbedItems:
    if item[1] in subbedValues:
        subbedValues[item[1]].append(item[0])
    else:
        subbedValues[item[1]] = [item[0]]
for item in addedItems:
    if item[1] in subbedValues:
        for key in subbedValues[item[1]]:
            print(f"{item[0]} = {key}   {item[1]} = {subbedResults[key]}")


