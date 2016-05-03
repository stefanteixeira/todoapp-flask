from todoapp.apps import app
import unittest

class ConfigUnitTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.app = app

    def test_dev_config(self):
        app.config.from_object('config.DevelopmentConfig')
        assert self.app.config['DEBUG'] is True
        assert self.app.config['DEVELOPMENT'] is True
        assert self.app.config['TESTING'] is True
        assert self.app.config['CSRF_ENABLED'] is False
        self.assertIn('sqlite:///',self.app.config['SQLALCHEMY_DATABASE_URI'])
        self.assertIn('todo.db',self.app.config['SQLALCHEMY_DATABASE_URI'])

    def test_stg_config(self):
        app.config.from_object('config.StagingConfig')
        assert self.app.config['DEBUG'] is True
        assert self.app.config['DEVELOPMENT'] is True
        assert self.app.config['TESTING'] is False
        assert self.app.config['CSRF_ENABLED'] is True
        self.assertIn('postgresql://admin:admin@postgres/todo',self.app.config['SQLALCHEMY_DATABASE_URI'])

class ToDoUnitTests(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.app = app.test_client()

    def test_pagenotfound_statuscode(self):
        result = self.app.get('/missing-page')

        self.assertEqual(result.status_code, 404)

    def test_pagenotfound_data(self):
        result = self.app.get('/missing-page')

        self.assertIn('Page Not Found', result.data)


if __name__ == "__main__":
    unittest.main()
