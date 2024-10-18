from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '_base.settings')

app = Celery('_base')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    "update contents average score in redis": {
        "task": "contents.tasks.update_average_score",
        "schedule": 5 * 60,
    }
}
