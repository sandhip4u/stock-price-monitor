from src.email_alert import send_email_alert

def test_send_email_alert():
    send_email_alert(
        subject="Test Alert",
        body="This is a test email",
        recipient_email="your_email@example.com"
    )
    assert True  # If no exception, pass
