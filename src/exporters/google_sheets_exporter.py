import gspread
from google.oauth2.service_account import Credentials


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]


def get_sheet():

    creds = Credentials.from_service_account_file(
        "credentials/google_credentials.json",
        scopes=SCOPES
    )

    client = gspread.authorize(creds)

    sheet = client.open(
        "Business Detector"
    ).sheet1

    return sheet


def export_to_google_sheet(businesses):

    if not businesses:
        print("No new businesses to export.")
        return

    sheet = get_sheet()

    for business in businesses:

        sheet.append_row([
            business["place_id"],
            business["name"],
            business["address"],
            business["phone"],
            business["website"],
            business["maps_url"]
        ])

    print(
        f"Exported {len(businesses)} businesses to Google Sheet."
    )