# posts.tasks

from django.core import management
from celery import shared_task

@shared_task
def connect():
    management.call_command('db_command')


