from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_booking_confirmation_email(booking_id, customer_email):
    subject = f'Booking Confirmation #{booking_id}'
    message = f'Your booking with ID {booking_id} has been successfully created.'
    send_mail(
        subject,
        message,
        'webmaster@example.com',  # From email
        [customer_email],
        fail_silently=False,
    )
