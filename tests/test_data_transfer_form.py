from selene.support.shared import browser
from selene import have

user_name = 'test name'
user_email = 'test@test.com'
user_addresses = 'test address'

def test_text_box_form(browser_manager):
    browser.open('https://demoqa.com/text-box')

    browser.element('.text-field-container #userName').type(user_name).press_tab()
    browser.element('#userEmail').type(user_email).press_tab()
    browser.element('#currentAddress').type(user_addresses).press_tab()
    browser.element('#permanentAddress').type(user_addresses).press_tab()
    browser.element('#submit').press_enter()

    browser.element('.col-md-12 #name').should(have.text(user_name))
    browser.element('.col-md-12 #email').should(have.text(user_email))
    browser.element('.col-md-12 #currentAddress').should(have.text(user_addresses))
    browser.element('.col-md-12 #permanentAddress').should(have.text(user_addresses))