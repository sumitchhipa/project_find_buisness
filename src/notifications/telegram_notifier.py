import requests

BOT_TOKEN = "8859148882:AAFK2J2V3WCnV3maVOYgo5nxG7Q7a7EQy1E"

CHAT_ID = "1199173572"


def send_telegram_notification(business):

    message = f"""
🚀 NEW BUSINESS FOUND

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

    url = (
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    )

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(
        url,
        data=payload
    )

    print(
        "Telegram Status:",
        response.status_code
    )