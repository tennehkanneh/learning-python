test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]

def find_largest(numbers):
    # Your code goes here
    leng_longest_str = 0
    
    for str in numbers :
        if leng_longest_str < len(str) :
            leng_longest_str = len(str)
    
    print(len(str))
    return len(str)



find_largest(test_strings)