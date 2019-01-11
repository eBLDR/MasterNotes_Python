"""
Setting up a headless browser, everything works normally without graphical interface.
"""


def quick_search(brow):
    try:
        brow.get('https://duckduckgo.com')

        search_form = brow.find_element_by_id('search_form_input_homepage')
        search_form.send_keys('python')
        search_form.submit()

        results = brow.find_elements_by_class_name('result')

        return results

    except Exception:
        print('Error while parsing the html - Element not found')

        return []


def display_results(r):
    print(type(r), len(r))

    for result in r:
        print(result.text)
        print('# ' * 20)


if __name__ == '__main__':
    from selenium.webdriver import Chrome
    # Importing options
    from selenium.webdriver.chrome.options import Options

    # Method #1
    opts = Options()
    # Setting to headless mode
    opts.set_headless()

    assert opts.headless  # Operating in headless mode

    # Pass the options object as parameter
    browser = Chrome(options=opts)

    """
    # Method #2

    # Create options object
    options = webdriver.ChromeOptions()

    # Add different arguments
    options.add_argument('headless')   # Headless mode
    options.add_argument('incognito')  # Incognito mode

    self.driver = webdriver.Chrome('chrome/driver/path', chrome_options=options)
    """

    res = quick_search(browser)
    display_results(res)

    # Closing the browser's process
    browser.quit()
