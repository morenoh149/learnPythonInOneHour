import random
import sys
import os

print("hello world")

# comment

'''
multi
line
comment
'''

name = "Derek"
print(name)

quote = "\"Always remember"

multi_line_quote = ''' just
like everyone else'''

new_string = quote + multi_line_quote

print("%s %s %s" % ('I like the quote', quote, multi_line_quote))
print("foo", end="") # omit newline
print("newlines")
