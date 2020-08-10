# REGULAR EXPRESSIONS
import re
mystr = "It was an amazing test." \
        " It was not at all about what we had learnt all these years." \
        " It just perfectly checks our presence of mind and how we respond to questions and situations that we are not  actually prepared for. " \
        "It tests where our brain is actually inclined towards." \
        " The type of questions asked in the test are very very logical and require a calm brain." \
        " What I learnt from the test was that, it is very important to be calm during the test, be relaxed and feel good." \
        " It is the kind of test that checks our brain's capacity,  interest and ability." \
        " The test was very interesting and everyone must definitely give it, not  to know how talented you are, but, to know where your own brain can outperform, and your innate wisdom. " \
        "The only preparation you need is nothing but readiness. " \
        "I thank Kapli Sir, Nikita Miss and team KPS for such an amazing experience."

# findall, search, split, sub, finditer
# findall - specific string matches.
# search - returns match object.
# split - split.
# sub -
# Meta Characters
# [] A set of characters.
# \ Signals a special sequence (can also be used to escape special sequences).
patt = re.compile(r'Miss')  # The raw string doesnt escape escape sequences.
patt = re.compile(r'.iss')  # (.) Any character (except newline character).
patt = re.compile(r'^It')  # (^) Starts with.
patt = re.compile(r'nce.$')  # ($) Ends with.
patt = re.compile(r'ai*')  # Zero or more occurrences.
patt = re.compile(r'a*i*')  # Zero or more occurrences.
patt = re.compile(r'ai+')  # One or more occurrences.
patt = re.compile(r'is{2}')  # Exactly the specified number of occurrences.
patt = re.compile(r'(is){2}')  # Capture and Group.
patt = re.compile(r'is{1}|t')  # Either Or.


# Special Sequences
# patt = re.compile(r'\AIt')  # Returns a match if the specified characters are at the beginning if the string..
# patt = re.compile(r'\bIt')  # Returns a match where the specified character is at the beginning or  at the end of a word.
# patt = re.compile(r'a\B')  # Returns the match where the specified characters are present .
# \w  # Returns a match where the string contains any word characters.
# \W  # Returns the match where the string DOES NOT contain a word character.
# \Z  # Returns the match if the specified characters are at the end of the string.
# \d  # Returns a match where the string contains digits (numbers from 0-9).
# \D  # Returns a match where the string DOES NOT contain digits.
# \s  # Returns a match where the string contains a whitespace character.
# \S  # Returns a match where the string DOES NOT contain whitespace character.
patt = re.compile(r'\d{5}-\d{4}')

matches = patt.finditer(mystr)
for match in matches:
        print(match)
        # print(mystr[812:816])

# TASK
# Given a string with a lot of indian phone numbers starting form +91.
# Return a list with all the numbers.
PhoneNumbers = "+91-9405678249,+91-9850833066,+91-8552031020,+91-9850567766"
patt1 = re.compile(r'\b+91-\d{10}')
Phone = patt1.finditer(PhoneNumbers)
for PhoneNo in Phone:
        print(PhoneNo)
