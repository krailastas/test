from celery import Celery

app = Celery('mxs')

app.config_from_object('django.conf:settings', namespace='CELERY')
