import pytest
from selene import browser, have

@pytest.fixture(scope="function", autouse=True)
def size_browser():
    browser.config.window_width = 1680
    browser.config.window_height = 1050
    yield
    browser.quit()

user_name = 'test name'
user_email = 'test@test.com'
user_addresses = 'test address'

def test_text_box_form():
    browser.open('https://demoqa.com/text-box')

    browser.element('.text-field-container [id="userName"]').type(user_name).press_tab()
    browser.element('#userEmail').type(user_email).press_tab()
    browser.element('#currentAddress').type(user_addresses).press_tab()
    browser.element('#permanentAddress').type(user_addresses).press_tab()
    browser.element('#submit').press_enter()

    browser.element('.col-md-12 [id=name]').should(have.text(user_name))
    browser.element('.col-md-12 [id=email]').should(have.text(user_email))
    browser.element('.col-md-12 [id=currentAddress]').should(have.text(user_addresses))
    browser.element('.col-md-12 [id=permanentAddress]').should(have.text(user_addresses))