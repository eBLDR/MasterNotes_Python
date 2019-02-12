# Regular expression - re module guide
import re

# Create a 'regex' object that contains the pattern to be searched for
# in the example, we will find phone numbers like 455-455-2535
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # using raw string to avoid typing many \ to escape \
print(phone_num_regex)
print(type(phone_num_regex))

msg_num = 'My personal number is 415-555-1212, work 333-777-0101'

# search() method will return the FIRST match
match_object = phone_num_regex.search(msg_num)  # if there is no match, None will be returned

if match_object:
    print(match_object)
    print(type(match_object))
    # group() method returns the whole match as str
    print('Phone number found: ' + match_object.group())

print('=' * 30)

# Creating groups with ()
phone_num_regex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex2.search(msg_num)
print(mo.group(1))  # to retrieve specific group, first group has number 1
print(mo.group(2))
print(mo.group(0))  # 0 is the default value, equivalent to mo.group()

print(mo.groups())  # to retrieve all the groups at once, returns a tuple

print('=' * 30)

# Using pipe character '|', several expressions positive match
hero_regex = re.compile(r'Batman|Jason')
print(hero_regex.search('You Jason, me Batman').group())

bat_regex = re.compile(r'Bat(man|mobile|copter)')
msg = 'Batmobile lost a wheel'
print(bat_regex.search(msg).group())
print(bat_regex.search(msg).group(1))

print('=' * 30)

# using ? for optional matches
bat_regex = re.compile(r'Bat(wo)?man')
msg = 'The adventures of Batwoman'
msg2 = 'The adventures of Batman'
print(bat_regex.search(msg).group())
print(bat_regex.search(msg2).group())

print('=' * 30)

# using * to match zero or more
banana_regex = re.compile(r'ba(na)*')  # will match 'ba' also
print(banana_regex.search('I like bananana').group())

# using + to match one or more
banana_regex = re.compile(r'ba(na)+')  # will match 'bana', but not 'ba'
print(banana_regex.search('I like bananana').group())

print('=' * 30)

# curly braces for range repetition
greedy_laugh_regex = re.compile(r'(Ha){3,5}')  # {min=0, max=infinite}, {,5} and {4,} also possible
print(greedy_laugh_regex.search('HaHaHaHa').group())

# python re are greedy by default, this means that they will match the longest string possible
# the non-greedy version matches the shortest possible
non_greedy_laugh_regex = re.compile(r'(Ha){3,5}?')  # place a ? after the closing curly brackets for non-greedy
print(non_greedy_laugh_regex.search('HaHaHaHa').group())

print('=' * 30)

# findall() method will return the str of every match found
mo = phone_num_regex.findall(msg_num)  # phoneNumRegex has no groups
print(mo)  # it's a list of str

mo2 = phone_num_regex2.findall(msg_num)  # phoneNumRegex2 has groups
print(mo2)  # in this case, it's a list of tuples

print('=' * 30)

# character classes can be mixed
band_regex = re.compile(r'\d+ \w+')  # 1+ digit followed by space followed by 1+ letter/digit/_
band = '12 drummers, 11 pipers, 10 trumpets, 7 violin, 1 voice, 1 piano'
print(band_regex.findall(band))

# character classes can also be personalized
vowel_regex = re.compile(r'[aeiouAEIOU]')
msg = 'Robocop eats food.'
print(vowel_regex.findall(msg))

# it's possible to include ranges using a hyphen when creating character classes
digits_and_letters_class = r'[a-zA-Z0-9]'
# inside square brackets the special characters are not interpreted as such, there is no need to scape them

# using ^ to create a negative character class
consonant_regex = re.compile(r'[^aeiouAEIOU]')  # all but excluding the ones in class
print(consonant_regex.findall(msg))

print('=' * 30)

# ^ to indicate string must start with the pattern
begins_with_hello = re.compile(r'^Hello')
print(begins_with_hello.search('Hello world!').group())

# $ to indicate string must end with the pattern
ends_with_number = re.compile(r'\d$')
print(ends_with_number.search('Your number is 24').group())

# combining both
whole_string_is_num = re.compile(r'^\d+$')
print(whole_string_is_num.search('12246302').group())

print('=' * 30)

# wildcard '.' to match everything but not newline
at_regex = re.compile(r'.at')
mo = at_regex.findall('The cat in the hat sat on the flat mat.')
print(mo)

# matching everything
name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: Edu Last Name: BLDR')
print(mo.group(1), mo.group(2))

# .* is greedy by default
msg = '<To serve man> for dinner.>'
greedy_regex = re.compile(r'<.*>')
print(greedy_regex.search(msg).group())

# for non-greedy, .*?
non_greedy_regex = re.compile(r'<.*?>')
print(non_greedy_regex.search(msg).group())

# DOTALL makes . match also newline
new_line_regex = re.compile('.*', re.DOTALL)  # this matches absolutely everything

print('=' * 30)

# case-insensitive matching, re.IGNORECASE = re.I
robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoBOcop is...').group())

print('=' * 30)

# substituting strings, .sub(newText, file)
secret_msg = 'Agent BLDR killed Agent Coka!'
secret_name_regex = re.compile(r'Agent \w+')
print(secret_name_regex.sub('CENSORED', secret_msg))

# if we want to replace some text but show some of the first letters
# \1 means enter text of group 1, \2 enter text of group 2 . . .
secret_name_regex2 = re.compile(r'Agent (\w)\w*')  # creating a group containing the first letter
print(secret_name_regex2.sub(r'\1*+-#', secret_msg))  # \1 for the group and desired text

# making life easier for complex patterns, re.VERBOSE ignores whitespaces and comments
phone_regex = re.compile(r'''(    # triple quotes for multi line string
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

# if we wish to combine different methods
modes_regex = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
