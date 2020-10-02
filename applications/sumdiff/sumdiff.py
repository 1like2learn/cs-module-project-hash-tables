"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
# Run the provided function on all the provided numbers
functionResults = {}
for num in q:
    functionResults[num] = f(num)

# Add the numbers together in all possible permeatations and store the result 
addedResults = {}
for num in q:
    for num2 in q:
        addedResults[f'f({num}) + f({num2})'] = functionResults[num] + functionResults[num2]

# Subtract the numbers from each other in all possible permeatations and store the result
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

# Make the dictionaries lists of touples so we can iterate over them
addedItems = list(addedResults.items())
subbedItems = list(subbedResults.items())

# Make an object of values. Each value has a list of the possible keys that produce it
subbedValues = {}
for item in subbedItems:
    if item[1] in subbedValues:
        subbedValues[item[1]].append(item[0])
    else:
        subbedValues[item[1]] = [item[0]]

# Compare every value in added items to ever key in subbedValues. If they are equal print every pair of values that 
for item in addedItems:
    if item[1] in subbedValues:
        for key in subbedValues[item[1]]:
            print(f"{item[0]} = {key}   {item[1]} = {subbedResults[key]}")


