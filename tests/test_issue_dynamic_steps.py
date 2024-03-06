import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_dynamic_steps():
    with allure.step("Открыть главную страницу github"):
        browser.open("/")

    with allure.step("Ввести поисковый запрос"):
        s(by.text('Search or jump to...')).click()
        s('#query-builder-test').send_keys("xanka359/Home_work_9")

    with allure.step("Выполнить поиск"):
        s('#query-builder-test').submit()

    with allure.step("Перейти в искомый репозиторий"):
        s(by.link_text("xanka359/Home_work_9")).click()
        s("#issues-tab").click()

    with allure.step("Найти issue по его номеру"):
        s(by.partial_text("#1")).should(be.visible)