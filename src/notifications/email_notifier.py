import smtplib

from email.mime.text import MIMEText


EMAIL_ADDRESS = "sumitchhipa001@gmail.com"

APP_PASSWORD = "ycalrqokdemenbha"


def send_email_notification(
    business
):

    subject = (
        f"NEW BUSINESS FOUND - "
        f"{business['name']}"
    )

    body = f"""
New Business Found

Name:
{business['name']}

Address:
{business['address']}

Phone:
{business['phone']}

Website:
{business['website']}

Maps URL:
{business['maps_url']}
"""

    message = MIMEText(body)

    message["Subject"] = subject
    message["From"] = EMAIL_ADDRESS
    message["To"] = EMAIL_ADDRESS

    with smtplib.SMTP(
        "smtp.gmail.com",
        587
    ) as server:

        server.starttls()

        server.login(
            EMAIL_ADDRESS,
            APP_PASSWORD
        )

        server.send_message(
            message
        )