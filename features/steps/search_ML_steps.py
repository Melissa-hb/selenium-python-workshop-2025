from behave import given, when, then
from selenium import webdriver
from pages.search_product import SearchProduct
@given('el usuario se encuentra en la pagina principal de mercado libre')
def step_given_intu_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.mercadolibre.com.co')
    context.search_product = SearchProduct(context.driver)

@when('el usuario escribe el producto iPhone 13')
def step_when_intu_login(context):
    context.search_product.search('iPhone 13')

@then('aparecen productos contienen el nombre iPhone')
def step_then_intu_login(context):
    assert "iPhone" in context.search_product.isElementPresent()
    

