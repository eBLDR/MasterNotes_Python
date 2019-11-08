"""
Graphic browser vs. headless browser.
"""
from timeit import timeit

from headless import quick_search
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.set_headless()

assert opts.headless


def run_graphic_chrome_browser():
    graphic_browser = Chrome()
    quick_search(graphic_browser)
    graphic_browser.quit()


def run_headless_chrome_browser():
    headless_browser = Chrome(options=opts)
    quick_search(headless_browser)
    headless_browser.quit()


reps = 20

graphic_chrome_time = timeit(run_graphic_chrome_browser, number=reps)
headless_chrome_time = timeit(run_headless_chrome_browser, number=reps)

print('Graphic Chrome browser took {} seconds.'.format(graphic_chrome_time))
print('Headless Chrome browser took {} seconds.'.format(headless_chrome_time))
