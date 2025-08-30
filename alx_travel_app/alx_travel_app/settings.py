# Celery configuration
CELERY_BROKER_URL = 'amqp://localhost'  # RabbitMQ default
CELERY_RESULT_BACKEND = 'rpc://'  # Optional
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
