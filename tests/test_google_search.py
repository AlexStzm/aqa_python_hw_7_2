import pytest
from selene.support.shared import browser
from selene import be, have

def test_valid_search_query():
    browser.open('https://google.com/ru')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))

def test_invalid_search_query():
    browser.open('https://google.com/ru')
    browser.element('[name="q"]').should(be.blank).type('dfgjlrdsjlgjfdsgkjdhfkhglfkdjxlbjfdbmcfnhbkdj').press_enter()
    browser.element('[id="search"]').should(have.text('Похоже, по вашему запросу нет полезных результатов'))