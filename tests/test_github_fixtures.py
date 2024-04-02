from selene import query
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_desktop_indirect(setup_browser_config_web):
    browser.open("https://github.com/")
    s('.HeaderMenu-link').get(query.attribute("/login"))


def test_mobile_indirect(setup_browser_config_mobile):
    browser.open("https://github.com/")
    s('[type = "button"]').get(query.attribute("/login"))
