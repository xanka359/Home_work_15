import pytest
from selene import query
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github_mobile_skip(setup_browser_config):
    if setup_browser_config == "mobile":
        pytest.skip("Это мобильное разрешение")
    browser.open("https://github.com/")
    s('.HeaderMenu-link').get(query.attribute("/login"))


def test_github_web_skip(setup_browser_config):
    if setup_browser_config == "desktop":
        pytest.skip("Это десктопное разрешение")
    browser.open("https://github.com/")
    s('[type = "button"]').get(query.attribute("/login"))
