import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")


def send_email(receiver_email: str, report: str):

    message = MIMEMultipart()

    message["From"] = EMAIL_ADDRESS
    message["To"] = receiver_email
    message["Subject"] = "Machine Maintenance Report"

    message.attach(MIMEText(report, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(message)

    return "Email sent successfully!"