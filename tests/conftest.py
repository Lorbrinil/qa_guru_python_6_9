import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def setup_browser_browser():
    browser.config.driver.set_window_size(1920, 1080)
