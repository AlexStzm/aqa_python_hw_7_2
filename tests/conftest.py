import pytest
from selene.support.shared import browser

@pytest.fixture(scope="function", autouse=True)
def browser_manager():
    browser.config.window_width = 1680
    browser.config.window_height = 1050
    yield
    browser.quit()