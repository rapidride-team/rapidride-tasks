from celery import Celery
import os

broker_url = os.getenv("BROKER_URL", "redis://localhost:6379/0")
backend_url = os.getenv("RESULT_BACKEND", "redis://localhost:6379/1")

celery_app = Celery("rapidride_tasks", broker=broker_url, backend=backend_url)
celery_app.autodiscover_tasks(["app.tasks"])
