import re
def remove_duplicate_words(text):
    return re.sub(r'(\b[a-z]+) \1', r'\1', text, flags=re.IGNORECASE)
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))#
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')) # re.sub substitutes duplicate consecutive words
test_string_with_punctuation = 'This is is a test test, a test of the system.'
print(remove_duplicate_words(test_string_with_punctuation))  # Outputs: This is is a test, a test of the system.