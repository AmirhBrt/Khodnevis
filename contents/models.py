from django.conf import settings
from django.core import validators
from django.db import models
from django_softdelete.models import SoftDeleteModel

from utils.models import TimeModel


class Content(SoftDeleteModel, TimeModel):
    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Contents'

    title = models.CharField(max_length=255, default='', blank=True)

    description = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Author',
        related_name='contents',
    )


class Rating(SoftDeleteModel, TimeModel):
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        constraints = (
            models.UniqueConstraint(
                fields=['content', 'rater'],
                name='unique_rating',
            ),
        )

    content = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
        verbose_name='Content',
        related_name='ratings',
    )

    rater = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Rater',
        related_name='ratings',
    )

    score = models.IntegerField(
        verbose_name='Score',
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(5)],
    )
