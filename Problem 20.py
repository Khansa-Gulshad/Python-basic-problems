# You are given a string S and width w.
# Your task is to wrap the string into a paragraph of width w.

import textwrap

def wrap(string, max_width):
    wrap=textwrap.fill(text=string, width=max_width) #fill join lines in a single block of text
    return wrap


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
