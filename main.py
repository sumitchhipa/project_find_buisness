from src.utils.config_loader import load_config

from src.exporters.csv_exporter import export_to_csv
from src.exporters.google_sheets_exporter import (
    export_to_google_sheet
)

from src.notifications.email_notifier import (
    send_email_notification
)
from src.notifications.telegram_notifier import (
    send_telegram_notification
)

from src.scraper.maps_scraper import (
    search_google_maps,
    get_business_links,
    scrape_business_details
)

from src.database.db import (
    create_tables,
    business_exists,
    save_business,
    get_total_businesses
)
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
APP_PASSWORD = os.getenv("APP_PASSWORD")
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def main():

    create_tables()

    config = load_config()

    postcodes = config["postcodes"]
    categories = config["categories"]

    total_new_businesses = []

    for postcode in postcodes:

        for category in categories:

            query = f"{category} in {postcode}"

            print("\n" + "=" * 80)
            print(f"RUNNING SEARCH: {query}")
            print("=" * 80)

            p, browser, page = search_google_maps(
                query
            )

            businesses = get_business_links(page)

            print(
                f"\nBusinesses Found: {len(businesses)}"
            )

            for business in businesses:

                try:

                    print(
                        f"\nScraping: {business['name']}"
                    )

                    details = scrape_business_details(
                        page,
                        business
                    )

                    if not details["place_id"]:
                        continue

                    if not business_exists(
                        details["place_id"]
                    ):

                        save_business(details)

                        total_new_businesses.append(
                            details
                        )
                        try:
                            send_telegram_notification( details )
                        except Exception as e:
                             print(
                                 f"TELEGRAM ERROR: {e}"
                                                         )

                        try:

                            send_email_notification(
                                details
                            )

                            print(
                                f"EMAIL SENT: "
                                f"{details['name']}"
                            )

                        except Exception as email_error:

                            print(
                                f"EMAIL ERROR: "
                                f"{email_error}"
                            )

                        print(
                            f"NEW BUSINESS FOUND: "
                            f"{details['name']}"
                        )

                    else:

                        print(
                            f"Already Exists: "
                            f"{details['name']}"
                        )

                except Exception as e:

                    print(
                        f"Error scraping "
                        f"{business['name']}"
                    )

                    print(e)

            browser.close()
            p.stop()

    # EXPORTS

    if total_new_businesses:

        export_to_csv(
            total_new_businesses
        )

        export_to_google_sheet(
            total_new_businesses
        )

        print(
            f"\nExported "
            f"{len(total_new_businesses)} "
            f"new businesses."
        )

    else:

        print(
            "\nNo new businesses found."
        )

    print("\n" + "=" * 80)

    print(
        f"Total Businesses In DB: "
        f"{get_total_businesses()}"
    )

    print(
        f"New Businesses Found: "
        f"{len(total_new_businesses)}"
    )

    print("=" * 80)


if __name__ == "__main__":
    main()