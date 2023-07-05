from selene.support import by
import allure
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from allure_commons.types import Severity


@allure.tag('Minor')
@allure.severity(Severity.MINOR)
@allure.label('owner', 's.popova')
@allure.story('Test Selene')
@allure.link("https://github.com", name="Testing")
def test_github():
    browser.open("https://github.com")

    s(".header-search-input").click()
    s(".header-search-input").send_keys("eroshenkoam/allure-example")
    s(".header-search-input").submit()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s("#issues-tab").click()

    s(by.partial_text("#76")).should(be.visible)
