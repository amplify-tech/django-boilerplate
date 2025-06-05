from celery import shared_task
import time


@shared_task
def send_welcome_email(user_id):
    print(f"Starting email task for user {user_id}...")
    time.sleep(5)  # Delay for 5 seconds
    print(f"Send done welcome email to user {user_id}")
