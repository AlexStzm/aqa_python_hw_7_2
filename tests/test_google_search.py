import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def open_browser():
    browser.open('https://google.com')

@pytest.fixture
def size_browser():
    browser.config.window_width = 1680
    browser.config.window_height = 1050

def test_valid_search_query(size_browser, open_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_invalid_search_query(size_browser, open_browser):
    browser.element('[name="q"]').should(be.blank).type('dfgjlrdsjlgjfdsgkjdhfkhglfkdjxlbjfdbmcfnhbkdj').press_enter()
    browser.element('[id="search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))