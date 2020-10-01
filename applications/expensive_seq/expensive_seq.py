# Your code here
cache = {}

def expensive_seq(x, y, z):
    # Your code here
    # If the provided values are in the cache return the cached value
    if (x,y,z) in cache:
        return cache[(x,y,z)]

    # If x is equal to zero return y + z. This is the base case
    if x <= 0:
        return y + z
    # If the values have not been cached and its not the base. 
    # Recursively compute these possible variations then cache the result for these variables
    if x >  0:
        v = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
        cache[(x,y,z)] = v
        return v



if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
