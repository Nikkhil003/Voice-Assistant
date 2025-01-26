# tests/test_email.py
from modules.email import send_email

def test_send_email():
    # Test sending an email (use a test email address)
    to = "test@example.com"
    content = "This is a test email."
    try:
        send_email(to, content)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")