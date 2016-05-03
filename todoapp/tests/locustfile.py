from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):
    @task
    def index(self):
        self.client.get("/")

    @task
    def new_todo(self):
        self.client.post('/new/', {
            "title": "Locust Test",
            "text": "Locust Test"
        })

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 2000
    max_wait = 5000
    host = "http://localhost:5000"
