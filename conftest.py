import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language with parameter, e.g.: --language=en")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    if lang:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--you must provide a language name such as --language=en")
    yield browser
    print("\nquit browser..")
    browser.quit()
