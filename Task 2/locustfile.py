from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://localhost:8000"  # <--- Укажи адрес своего тестируемого приложения

    @task
    def load_main_page(self):
        self.client.get("/")
