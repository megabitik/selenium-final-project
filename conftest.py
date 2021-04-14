import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language with parameter, e.g.: --language=en")
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    # Check if browser is chosen correctly. Chrome is set by default.
    browser_name = request.config.getoption("browser_name")
    browser = None

    # Set language for pages - browser's "accept-language" option ('en' by default)
    # And set the browser - chrome of firefox (Chrome by default)
    lang = request.config.getoption("language")
    if lang:
        if browser_name == 'chrome':
            options = Options()
            options.add_experimental_option('prefs', {'intl.accept_languages': lang})
            browser = webdriver.Chrome(options=options)
        elif browser_name == 'firefox':
            webdriver.FirefoxProfile().set_preference("intl.accept_languages", lang)
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    else:
        raise pytest.UsageError("--you must provide a language name such as --language=en")

    #yield
    yield browser
    print("\nquit browser..")
    browser.quit()
