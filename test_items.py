from selenium.webdriver.common.by import By
import time

link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_cart_button(browser):
    browser.get(link)
    # time.sleep(30) # Sleep for 10 seconds if you want to check the language manually
    add_to_basket_button =  browser.find_element(By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")
    assert add_to_basket_button, "Add to basket button is not found."