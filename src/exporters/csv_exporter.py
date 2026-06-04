import csv
from pathlib import Path

CSV_PATH = Path("data/new_businesses.csv")


def export_to_csv(businesses):

    if not businesses:
        return

    file_exists = CSV_PATH.exists()

    with open(
        CSV_PATH,
        "a",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "place_id",
                "name",
                "address",
                "phone",
                "website",
                "maps_url"
            ]
        )

        if not file_exists:
            writer.writeheader()

        writer.writerows(businesses)