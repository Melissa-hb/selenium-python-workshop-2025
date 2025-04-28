from behave import given, when, then
from selenium import webdriver
from pages.search_wikipedia import Search
@given('el usuario se encuentra en la pagina principal de wikipedia')
def step_given_intu_login(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')
    context.search_wikipedia = Search(context.driver)

@when('el usuario escribe el tema Python (lenguaje de programación) en el buscador')
def step_when_intu_login(context):
    context.search_wikipedia.search('Python (lenguaje de programación)')

@then('aparece el titulo Python')
def step_then_intu_login(context):
    assert "Python" == context.search_wikipedia.isElementPresent()
    

