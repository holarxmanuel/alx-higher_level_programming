#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        first_char = None
    else:
        first_char = sentence[0]
    
    return len(sentence), first_char

# Example usage:
result = multiple_returns("Hello, world!")
print(result)  # Output: (13, 'H')
