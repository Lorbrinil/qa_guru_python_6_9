import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag('Critical')
@allure.severity(Severity.CRITICAL)
@allure.label('owner', 's.popova')
@allure.story('Test Selene Decorator')
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue()
    should_see_issue_with_number('#76')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-input').click()
    s('.header-search-input').send_keys(repo)
    s('.header-search-input').submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем таб Issue')
def open_issue():
    s('#issues-tab').click()


@allure.step('Ищем номер {number}')
def should_see_issue_with_number(number):
    s(by.partial_text(number)).should(be.visible)
