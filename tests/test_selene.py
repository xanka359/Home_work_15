from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("/")


    browser.element(by.text('Search or jump to...')).click()
    browser.element('#query-builder-test').send_keys("eroshenkoam/allure-example")
    browser.element('#query-builder-test').submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)
