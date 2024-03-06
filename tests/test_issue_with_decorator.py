import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.step("Открыть главную страницу github")
def open_main_page():
    browser.open("/")

@allure.step("Ввести поисковый запрос")
def type_query():
    s(by.text('Search or jump to...')).click()
    s('#query-builder-test').send_keys("xanka359/Home_work_9")

@allure.step("Выполнить поиск")
def confirm_query():
    s('#query-builder-test').submit()

@allure.step("Перейти в искомый репозиторий")
def deep_into_rep():
    s(by.link_text("xanka359/Home_work_9")).click()
    s("#issues-tab").click()

@allure.step("Найти issue по его номеру")
def search_issue():
    s(by.partial_text("#0")).should(be.visible)

def test_with_decorator():
    open_main_page()
    type_query()
    confirm_query()
    deep_into_rep()
    search_issue()