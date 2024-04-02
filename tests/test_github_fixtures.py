from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_desktop_indirect(setup_browser_config_web):
    browser.open("https://github.com/")
    browser.all('[href="/login"]').second.click()


def test_mobile_indirect(setup_browser_config_mobile):
    browser.open("https://github.com/")
    s('[href="/login"]').click()
