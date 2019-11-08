"""
The selenium module lets Python directly control the browser by
programmatically clicking links and filling in login information, almost as a
human user interacting with the page.

selenium needs the driver corresponding to the desired browser in use to be
installed.
"""
from selenium import webdriver

# Specific driver import
# from selenium.webdriver import Chrome

# The browser's driver must be installed, otherwise an error will be raised
browser = webdriver.Chrome()  # This will start and open the browser
print(type(browser))

try:
    # Sends http get method to the URL - directs the browser
    browser.get('https://www.python.org/')
    print(browser.current_url)

except Exception:
    print('Invalid URL.')

"""
### Method - Returned Web element
* = find_element or find_elements
find_element returns the first matching element
find_elements returns a list of matching elements

browser.*_by_class_name(name) - Elements that use the CSS class name

browser.*_by_css_selector(selector) - Elements that match the CSS selector

browser.*_by_id(id) - Elements with a matching id attribute value

browser.*_by_link_text(text) - <a> elements that completely match the text
provided

browser.*_by_partial_link_text(text) - <a> elements that contain the text
provided

browser.*_by_name(name) - Elements with a matching name attribute value

browser.*_by_tag_name(name) - Elements with a matching tag name (case
insensitive)

### Attr/Method - Description

tag_name - The tag name, such as 'a' for an <a> element

get_attribute(name) - The value for the element’s name attribute

text - The text within the element, such as 'hello' in <span>hello</span>

clear() - For text field or text area elements, clears the text typed into it

is_displayed() - Returns True if the element is visible; otherwise returns
False

is_enabled() - For input elements, returns True if the element is enabled;
otherwise returns False

is_selected() - For checkbox or radio button elements, returns True if the
element is selected; otherwise returns False

location - A dictionary with keys 'x' and 'y' for the position of the element
in the page
"""

print('=' * 30)

# Finding one element
elem_name = 'python-logo'
try:
    elem = browser.find_element_by_class_name(elem_name)
    print('Found {} element with a matching name'.format(elem.tag_name))
    print(type(elem))
except Exception:
    print('Not able to find an element with a matching name.')

print('=' * 30)

# Finding and clicking on a link
link_text = 'Downloads'
try:
    link_elem = browser.find_element_by_link_text(link_text)
    print('Link found.')
    print(type(link_elem))
    # Clicking will follow the link
    link_elem.click()
except Exception:
    print('Not able to find a link containing that text.')

print('=' * 30)

# Filling and submitting forms
elem_id = 'id-search-field'
search_text = 'new release'
try:
    search_elem = browser.find_element_by_id(elem_id)
    print('Element found.')
    print(type(search_elem))
    # Filling the form with data
    search_elem.send_keys(search_text)
    # Submitting the form
    search_elem.submit()
    print('Form filled and submitted.')
except Exception:
    print('Not able to find an element with a matching id.')

"""
Special keys
DOWN, UP, LEFT, RIGHT, ENTER, RETURN, HOME, END, ESCAPE, BACK_SPACE, DELETE,
TAB, PAGE_UP, PAGE_DOWN, F1, ..., F12, ... and more.
"""
# Module containing the keys
from selenium.webdriver.common.keys import Keys

try:
    # To send keys, the best place is the general web page, using <html> tag
    html_elem = browser.find_element_by_tag_name('html')
    html_elem.send_keys(Keys.END)  # Scrolls to the bottom
except Exception:
    print('Not able to find <html> tag_name.')

# Clicking browser buttons
# browser.back()
# browser.forward()
# browser.refresh()
# browser.quit()

# Closing the browser
# browser.Close() - Close the browser window that the driver has focus of
# browser.Quit() - Calls Dispose()
# browser.Dispose() Closes all browser windows and safely ends the session
