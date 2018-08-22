"""
Web scraping is data scraping used for extracting data from websites.
requests module lets us easily download files from the Web,
managing network errors, connection problems and data compression.
"""

import requests

# get() function takes a str of a URL where to download data from,
# and returns a str object with the data
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')

# it's important to check the status after calling the get() method
try:
    res.raise_for_status()  # this method will raise and exception if there was an
                            # error downloading the file, otherwise will do nothing
                            # 404 Client Error: Not Found for url: . . .
    print('Status: OK')

except Exception as exc:
    print('There was a problem: {}'.format(exc))


print(type(res))  # it's a response object

print(len(res.text))  # text from url saved as str
print(res.text[:70])

# saving the text on a file
with open('rjtext.txt', 'wb') as file:      # mode must be 'wb', to write in binary, to maintain the Unicode Encoding
    for chunk in res.iter_content(10000):   # the argument is the size of the 'chunk' of data on each iteration
        file.write(chunk)

print('=' * 50)

# scraping HTML page source
res2 = requests.get('https://en.wikipedia.org/wiki/Siamese_fighting_fish')
res2.raise_for_status()
print(len(res2.text))
print(res2.text[:150])

# at this point, we could use regular expressions to parse the html source and search for whatever is necessary

# saving the text (.html) on a file
with open('htmlscrap.html', 'wb') as file:
    for chunk in res2.iter_content(10000):
        file.write(chunk)
