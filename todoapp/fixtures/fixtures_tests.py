from todoapp.apps import app, db
import unittest
from todoapp.models import Todo
from flask.ext.fixtures import FixturesMixin

FixturesMixin.init_app(app, db)

class ToDoFixturesTests(unittest.TestCase, FixturesMixin):

    fixtures = ['todos.yaml']

    def test_todos(self):
        todos = Todo.query.all()
        assert len(todos) == Todo.query.count() == 3

    def test_exist_todo_first(self):
        todo1 = Todo.query.first()
        self.assertEquals(todo1.title, 'Fixture TODO 1')
        self.assertEquals(todo1.text, 'Fixture TODO 1 - Text')

if __name__ == "__main__":
    unittest.main()
