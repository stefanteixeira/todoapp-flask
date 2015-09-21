from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

driver.implicitly_wait(10)
driver.get("http://localhost:5000")
if not "TodoApp" in driver.title:
    raise Exception("Unable to load page!")

btnNewTodo = driver.find_element_by_id("new")
btnNewTodo.click()

title = driver.find_element_by_id("title")
text = driver.find_element_by_id("text")
btnCreate = driver.find_element_by_id("save")

title.send_keys("New TODO")
text.send_keys("Describe the task clearly")
btnCreate.click()

assert driver.current_url == "http://localhost:5000/"

driver.quit()
