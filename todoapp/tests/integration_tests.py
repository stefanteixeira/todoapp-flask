from todoapp.apps import app,db
import unittest
from todoapp.models import Todo

class ToDoUnitTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.app = app.test_client()
        db.create_all()

    @classmethod
    def tearDownClass(self):
        db.session.remove()
        db.drop_all()

    def test_home_empty(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status_code, 200)
        assert 'All Items' in rv.data

    def test_new_todo(self):
        self.app.post('/new/', data=dict(title='Unit Test 2', text= 'Unit Test Description 2'))
        rv = self.app.get('/')
        assert 'Unit Test 2' in rv.data
        assert 'Unit Test Description 2' in rv.data

    def test_show_todo(self):
        rv = self.app.get('/todos/1')
        assert 'Unit Test 2' in rv.data
        assert 'Unit Test Description 2' in rv.data

    def test_update_todo(self):
        self.app.post('/todos/1', data=dict(title='Unit Test Updated', text= 'Unit Test Description Updated'))
        rv = self.app.get('/')
        assert 'Unit Test 2' not in rv.data
        assert 'Unit Test Description 2' not in rv.data
        assert 'Unit Test Updated' in rv.data
        assert 'Unit Test Description Updated' in rv.data


if __name__ == "__main__":
    unittest.main()
