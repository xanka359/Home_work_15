from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_github():
    browser.open("/")

    s(by.text('Search or jump to...')).click()
    s('#query-builder-test').send_keys("xanka359/Home_work_9")
    s('#query-builder-test').submit()

    s(by.link_text("xanka359/Home_work_9")).click()
    s("#issues-tab").click()
    s(by.partial_text("#1")).should(be.visible)