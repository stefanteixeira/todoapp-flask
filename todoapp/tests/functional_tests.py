from selenium import webdriver
import unittest

class ToDoFunctionalTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def test_create_todo(self):
        self.driver.get(u'http://localhost:5000/')
        if not "TodoApp" in self.driver.title:
            raise Exception("Unable to load page!")
        btn_new_todo = self.driver.find_element_by_id("new")
        btn_new_todo.click()

        title = self.driver.find_element_by_id("title")
        text = self.driver.find_element_by_id("text")
        btn_create = self.driver.find_element_by_id("save")

        title.send_keys("New TODO")
        text.send_keys("Describe the task clearly")
        btn_create.click()

        assert self.driver.current_url == u'http://localhost:5000/'
        page_source = self.driver.page_source
        assert "New TODO" in page_source
        assert "Describe the task clearly" in page_source

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
