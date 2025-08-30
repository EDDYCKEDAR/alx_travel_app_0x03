# ALX Travel App 0x03

## Background Task Setup with Celery + RabbitMQ

### 1. Install RabbitMQ
```bash
sudo apt-get install rabbitmq-server
sudo service rabbitmq-server start
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Run Django migrations
bash
Copy code
python manage.py migrate
4. Start Celery worker
bash
Copy code
celery -A alx_travel_app worker -l info
5. Test Booking Email
Create a booking via the API or admin panel.

Verify email is sent asynchronously via console or SMTP backend.
