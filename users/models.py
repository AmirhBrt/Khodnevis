from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """The base Khodnevis user who is enabled to post or like a content."""
    pass
