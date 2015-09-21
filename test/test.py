from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.implicitly_wait(10)
driver.get("http://localhost:5000/")
if not "TodoApp" in driver.title:
    raise Exception("Unable to load google page!")
btnNewTodo = driver.find_element_by_id("new")
btnNewTodo.click()
print driver.title

driver.quit()
