import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
APP_PASSWORD = os.environ.get("APP_PASSWORD")

def send_reminder(recipient_email: str):
    """
    Sends an abusive (behavior-enforcing) reminder email using Gmail SMTP.
    """
    if not SENDER_EMAIL or not APP_PASSWORD:
        print("ERROR: SENDER_EMAIL or APP_PASSWORD not set in .env")
        return False
        
    msg = EmailMessage()
    msg['Subject'] = 'LeetCode Daily Accountability Reminder'
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg.set_content("You haven't solved a LeetCode problem today. Stop being lazy and get it done.")

    try:
        # Gmail SMTP setup
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
            print(f"[{recipient_email}] Reminder email sent successfully!")
            return True
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")
        return False

if __name__ == "__main__":
    # Test the function (will fail if .env not configured)
    test_email = "mock.email@example.com"
    send_reminder(test_email)
