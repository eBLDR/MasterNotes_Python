"""
Taking a screenshot of the window (even if it's running in headless mode.
"""
from selenium.webdriver import Chrome

browser = Chrome()
browser.get('https://duckduckgo.com')

# Taking the screenshot and saving the file in path/file/name
browser.get_screenshot_as_file('myscreenshot.png')

# Equivalent to
browser.save_screenshot('myscreenshot.png')
browser.quit()
