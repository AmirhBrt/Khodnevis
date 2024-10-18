from django.core.cache import caches

default_cache = caches['default']
default_redis = default_cache.client.get_client()
default_pipeline = default_redis.pipeline()
