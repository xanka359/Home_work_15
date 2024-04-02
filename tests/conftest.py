from selene import browser
import pytest


@pytest.fixture(params=[('1920', '1080'), ('1680', '1050')], scope='function')
def setup_browser_config_web(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[('360', '640'), ('360', '740')], scope='function')
def setup_browser_config_mobile(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[('1920', '1080'), ('480', '853')], scope='function')
def setup_browser_config(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if int(width) > 800:
        yield "desktop"
    else:
        yield "mobile"

    browser.quit()
