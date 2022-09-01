# blog.celery

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

app = Celery('blog')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# start the scheduler
# # celery -A blog beat

# start the worker
# # celery -A blog worker --loglevel=INFO --concurrency 1 -P solo

# start redis broker
# # redis-server

# Monitor with flower
# # celery -A hacker flower