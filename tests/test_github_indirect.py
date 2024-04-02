import pytest
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@pytest.mark.parametrize("setup_browser_config_web", [('1920', '1080'), ('1680', '1050')], indirect=True)
def test_desktop_indirect(setup_browser_config_web):
    browser.open("https://github.com/")
    browser.all('[href="/login"]').second.click()


@pytest.mark.parametrize("setup_browser_config_mobile", [('360', '640'), ('360', '740')], indirect=True)
def test_mobile_indirect(setup_browser_config_mobile):
    browser.open("https://github.com/")
    s('[href="/login"]').click()
