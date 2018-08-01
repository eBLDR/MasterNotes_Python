"""
# re module guide

- Character Classes -
\d - matches any decimal digit; equivalent to the class [0-9].
\D - matches any non-digit character; equivalent to the class [^0-9].
\s - matches any whitespace character; equivalent to the class [ \t\n\r\f\v].
\S - matches any non-whitespace character; equivalent to the class [^ \t\n\r\f\v].
\w - matches any alphanumeric character and underscore; equivalent to the class [a-zA-Z0-9_].
\W - matches any non-alphanumeric character nor underscore; equivalent to the class [^a-zA-Z0-9_]

Personalized classes are possible: [\s,.] - will match \s, ',' and '.'

If any of the special characters need to be used in the regex object for patter searching
we will use the scape character \. e.g.: (r'(\(\d\d\d\))') will match (123), for example

- Special Characters -
Greedy by default:
()  - to create groups - (r'(\d\d\d)-(\d\d\d)')
|   - pipe, used to match one of many expressions - (r'Bat(man|mobile|copter)')
?   - optionally matching character/group - (r'Bat(wo)?man')
*   - match zero or more of the preceding character/group - (r'Bat(wo)*man')
+   - match one or more of the preceding character/group - (r'Bat(wo)+man')
{}  - matching specific/range repetitions (greedy version) - (r'(Ha{3}') - (r'(Ha){3,5}')
^   - beginning must match - (r'^Hello')
$   - end must match - (r'\d$')
[]  - to create character classes - (r'[aeiou]') - (r'[\d+ \w+]')
[^] - to create negative character classes - (r'[^aeiou]')
.   - wildcard, matches everything except for newline
Non-greedy:
{}? - non-greedy version of {} - (r'(Ha){3,5}?')
*?  - non-greedy version of * 
+?  - non-greedy version of +
"""

import re

# create a 'regex' object that contains the pattern to be searched for
# in the example, we will find phone numbers like 455-455-2535
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # using raw string to avoid typing many \ to escape \
print(phoneNumRegex)
print(type(phoneNumRegex))

msgNum = 'My personal number is 415-555-1212, work 333-777-0101'

# search() method will return the FIRST match
matchObject = phoneNumRegex.search(msgNum)  # if there is no match, None will be returned

if matchObject:
    print(matchObject)
    print(type(matchObject))
    # group() method returns the whole match as str
    print('Phone number found: ' + matchObject.group())
    
print("=" * 30)

# creating groups with ()
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex2.search(msgNum)
print(mo.group(1))  # to retrieve specific group, first group has number 1
print(mo.group(2))
print(mo.group(0))  # 0 is the default value, equivalent to mo.group()

print(mo.groups())  # to retrieve all the groups at once, returns a tuple

print("=" * 30)

# using pipe character '|', several expressions positive match
heroRegex = re.compile(r'Batman|Jason')
print(heroRegex.search('You Jason, me Batman').group())

batRegex = re.compile(r'Bat(man|mobile|copter)')
msg = 'Batmobile lost a wheel'
print(batRegex.search(msg).group())
print(batRegex.search(msg).group(1))

print("=" * 30)

# using ? for optional matches
batRegex = re.compile(r'Bat(wo)?man')
msg = 'The adventures of Batwoman'
msg2 = 'The adventures of Batman'
print(batRegex.search(msg).group())
print(batRegex.search(msg2).group())

print("=" * 30)

# using * to match zero or more
bananaRegex = re.compile(r'ba(na)*')  # will match 'ba' also
print(bananaRegex.search('I like bananana').group())

# using + to match one or more
bananaRegex = re.compile(r'ba(na)+')  # will match 'bana', but not 'ba'
print(bananaRegex.search('I like bananana').group())

print("=" * 30)

# curly braces for range repetition
greedyLaughRegex = re.compile(r'(Ha){3,5}')  # {min=0, max=infinite}, {,5} and {4,} also possible
print(greedyLaughRegex.search('HaHaHaHa').group())

# python re are greedy by default, this means that they will match the longest string possible
# the non-greedy version matches the shortest possible
nongreedyLaughRegex = re.compile(r'(Ha){3,5}?')  # place a ? after the closing curly brackets for non-greedy
print(nongreedyLaughRegex.search('HaHaHaHa').group())

print("=" * 30)

# findall() method will return the str of every match found
mo = phoneNumRegex.findall(msgNum)  # phoneNumRegex has no groups
print(mo)  # it's a list of str

mo2 = phoneNumRegex2.findall(msgNum)  # phoneNumRegex2 has groups
print(mo2)  # in this case, it's a list of tuples

print("=" * 30)

# character classes can be mixed
bandRegex = re.compile(r'\d+ \w+')  # 1+ digit followed by space followed by 1+ letter/digit/_
band = '12 drummers, 11 pipers, 10 trumpets, 7 violin, 1 voice, 1 piano'
print(bandRegex.findall(band))

# character classes can also be personalized
vowelRegex = re.compile(r'[aeiouAEIOU]')
msg = 'Robocop eats food.'
print(vowelRegex.findall(msg))

# it's possible to include ranges using a hyphen when creating character classes
digitsAndLettersClass = r'[a-zA-Z0-9]'
# inside square brackets the special characters are not interpreted as such, there is no need to scape them

# using ^ to create a negative character class
consonantRegex = re.compile(r'[^aeiouAEIOU]')  # all but excluding the ones in class
print(consonantRegex.findall(msg))

print("=" * 30)

# ^ to indicate string must start with the pattern
beginsWithHello = re.compile(r'^Hello')
print(beginsWithHello.search('Hello world!').group())

# $ to indicate string must end with the pattern
endsWithNumber = re.compile(r'\d$')
print(endsWithNumber.search('Your number is 24').group())

# combining both
wholeStringIsNum = re.compile(r'^\d+$')
print(wholeStringIsNum.search('12246302').group())

print("=" * 30)

# wildcard '.' to match everything but not newline
atRegex = re.compile(r'.at')
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

# matching everything
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Edu Last Name: BLDR')
print(mo.group(1), mo.group(2))

# .* is greedy by default
msg = '<To serve man> for dinner.>'
greedyRegex = re.compile(r'<.*>')
print(greedyRegex.search(msg).group())

# for non-greedy, .*?
nongreedyRegex = re.compile(r'<.*?>')
print(nongreedyRegex.search(msg).group())

# DOTALL makes . match also newline
newLineRegex = re.compile('.*', re.DOTALL)  # this matches absolutely everything

print("=" * 30)

# case-insensitive matching, re.IGNORECASE = re.I
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoBOcop is...').group())

print("=" * 30)

# substituting strings, .sub(newText, file)
secretMsg = 'Agent BLDR killed Agent Coka!'
secretNameRegex = re.compile(r'Agent \w+')
print(secretNameRegex.sub('CENSORED', secretMsg))

# if we want to replace some text but show some of the first letters
# \1 means enter text of group 1, \2 enter text of group 2 . . .
secretNameRegex2 = re.compile(r'Agent (\w)\w*')  # creating a group containing the first letter
print(secretNameRegex2.sub(r'\1*+-#', secretMsg))  # \1 for the group and desired text

# making life easier for complex patterns, re.VERBOSE ignores whitespaces and comments
phoneRegex = re.compile(r'''(     # triple quotes for multiline string
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# if we wish to combine different methos
modesRegex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
