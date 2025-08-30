# Celery configuration
CELERY_BROKER_URL = 'amqp://localhost'  # RabbitMQ default
CELERY_RESULT_BACKEND = 'rpc://'  # Optional
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
# Email configuration
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # for testing
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-email-password'
DEFAULT_FROM_EMAIL = 'webmaster@example.com'
