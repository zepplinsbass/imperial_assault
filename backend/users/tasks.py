from django.core import management

from imperial-assault import celery_app


@celery_app.task
def clearsessions():
    management.call_command('clearsessions')
