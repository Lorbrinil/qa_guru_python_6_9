import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


@allure.tag('Normal')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 's.popova')
@allure.story('Test Selene Lambda')
@allure.link("https://github.com", name="Testing")
def test_lambda_steps():
    with allure.step(('Открываем главную страницу')):
        browser.open('https://github.com')

    with allure.step(('Ищем репозиторий')):
        s('.header-search-input').click()
        s('.header-search-input').send_keys('eroshenkoam/allure-example')
        s('.header-search-input').submit()

    with allure.step(('Переходим по ссылке репозитория')):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step(('Открываем таб Issue')):
        s('#issues-tab').click()

    with allure.step(('Ищем номер 76')):
        s(by.partial_text('#76')).should(be.visible)
