from celery import shared_task
from django.db import models

from contents.models import Content
from utils.redis import default_pipeline


@shared_task
def update_average_score():
    contents = Content.objects.annotate(avg=models.Avg('ratings__score')).values('id', 'avg')
    for content in contents:
        default_pipeline.set(f"contents:average_score:{content['id']}", content['avg'] or 0.0)
    default_pipeline.execute()
