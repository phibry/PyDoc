# Finding repetition
# Finding text
import re

# patterns = ["term1", "term2"]
# text = "This is a string with term1, but no the other term"

# # print(re.search("hello", "hello world"))

# # for pattern in patterns:
# #     print(f"Searching for {pattern}, in \n{text}")

# #     # check for match
# #     if re.search(pattern, text):
# #         print("\n")
# #         print("Match was found\n")
# #     else:
# #         print("\n")
# #         print("No Match was found.\n")

# # print(re.search("h", "w")) # no match

# match = re.search(patterns[0], text)
# print(type(match))  # class object, you can run methods on it

# print(match.start())
# print(match.end())


# # Split with regular expression
# split_term = "@"

# phrase = "What is your email, is it hello@gmail.com?"
# # split at term @
# splited = re.split(split_term, phrase)
# print(splited)
# # same as
# print("hello world".split())


# matches = re.findall("match", "here is one match, here is another match")
# print(matches)
# find all instances of match
# print(len(matches))


def multi_re_find(patterns, phrase):
    """
    Takes in a list of regex patterns
    Prints a list of all matches
    """
    for pattern in patterns:
        print(f"Searching the phrase using the re check: {pattern}")
        print(re.findall(pattern, phrase))
        print("\n")


### Repetition Syntax
test_phrase = "sdsd..sssddd...sdddsddd...dsds...dssss...sdddd"
test_patterns = ["sd*", "sd+", "sd?", "sd{3}", "sd{2,3}"]
# *      take an s and followed by zero or more d's
# +      s followed by one ore more d's
# ?      s followed by zero or one d's
# {3}    s followed by three d's
# {2,3}  s followed by two or three d's
# multi_re_find(test_patterns, test_phrase)


### Character Sets
test_phrase = "sdsd..sssddd...sdddsddd...dsds...dssss...sdddd"
test_patterns = ["[sd]", "s[sd]+"]
# [sd]      either s or d
# s[sd]+    s followed by one or more s or d
# multi_re_find(test_patterns, test_phrase)


### Exclusion
test_phrase = "This is a string! But it has punctuation. How can we remove it?"
# print(re.findall("[^!.? ]+", test_phrase))
# +, if it hase more

### Character Ranges
test_phrase = "This is an example sentenc. Lets see if we can find some letters"
test_patterns = ["[a-z]+", "[A-Z]+", "[a-zA-Z]+", "[A-Z][a-z]+"]
# [a-z]+        sequences of lower case letters
# [A-Z]+        sequences of upper case letters
# [a-zA-Z]+     sequences of lower or upper case letters
# [A-Z][a-z]+   one upper cas letter followed by a lower case letter

# multi_re_find(test_patterns, test_phrase)


### Excape Codes
# Find Pattern
# \d    a digit
# \D    a non-digit
# \s    whitespace(tab, space, newline, etc.)
# \S    non-whitespace
# \w    alphanumeric
# \W    non-alphanumeric
print("hello \n new line")

test_phrase = "This is a string with some numbers 1233 and a symbol #hashtag"
test_patterns = [r"\d+", r"\D+", r"\s+", r"\S+", r"\w+", r"\W+"]
multi_re_find(test_patterns, test_phrase)
