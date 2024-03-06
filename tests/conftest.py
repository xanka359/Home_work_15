from selene import browser
import pytest


@pytest.fixture(scope='session', autouse=True)
def manage_browser():
    browser.config.base_url = 'https://github.com/'
    browser.config.window_height = 1080  # задает высоту окна браузера
    browser.config.window_width = 1920

    yield
    browser.quit()