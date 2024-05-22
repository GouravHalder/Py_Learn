import reprlib
s = 'Hello, world.' * 10  # Create a long string by repeating 'Hello, world.'
shortened_repr = reprlib.repr(s) #  it truncates the output to a more manageable length, adding ellipses (...) to indicate that the representation has been shortened.
print(shortened_repr)

"""The pprint module in Python stands for "pretty-print" 
and is used to print data structures in a formatted and more readable way. 
This module is particularly useful for printing nested data structures 
such as lists and dictionaries, where the default print behavior might be hard to read."""

import pprint
data = {
    'name': 'John',
    'age': 30,
    'children': [
        {'name': 'Jane', 'age': 10},
        {'name': 'Jack', 'age': 8}
    ],
    'pets': ['dog', 'cat']
}
pprint.pprint(data)

#The textwrap module formats paragraphs of text to fit a given screen width:
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))

#Templating format uses placeholder names formed by $ with valid Python identifiers (alphanumeric characters and underscores). 
from string import Template
# Correctly define the template with placeholders
t = Template('Hello ${place1} how r u')
# Substitute the placeholder with the actual values
result = t.substitute(place1='Kolkata')
# Print the result
print(result)