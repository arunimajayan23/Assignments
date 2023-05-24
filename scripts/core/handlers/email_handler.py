from fastapi import FastAPI
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from schemas.models import Email

app = FastAPI()


def send_email(body, email: Email):
    # Set up the email details
    sender_email = "arunimajayana@gmail.com"
    sender_password = "tzsvusnuhketxdwe"
    receiver_email = email.rec_email

    # Create a multipart message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Total Amount Received"

    # Add the body to the email
    message.attach(MIMEText(body, "html"))

    try:
        # Create a secure connection to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to the sender's email account
        server.login(sender_email, sender_password)

        # Send the email
        server.send_message(message)

        # Close the connection
        server.quit()

        return {"message": "Email sent successfully"}
    except Exception as e:
        return {"message": str(e)}
