import re
from urllib.parse import unquote

from playwright.sync_api import sync_playwright


def extract_place_id(url: str):
    """
    Extract unique Google Maps place identifier
    """

    match = re.search(
        r'!1s([^!]+)!',
        url
    )

    if match:
        return match.group(1)

    return None


def search_google_maps(query: str):

    p = sync_playwright().start()

    browser = p.chromium.launch(
        headless=False,
        slow_mo=500
    )

    page = browser.new_page()

    print("Opening Google Maps...")

    page.goto(
        "https://www.google.com/maps",
        wait_until="domcontentloaded",
        timeout=120000
    )

    page.wait_for_timeout(5000)

    print("Finding search box...")

    search_box = page.get_by_role(
        "combobox",
        name="Search Google Maps"
    )

    search_box.click()

    search_box.fill(query)

    print(f"Searching: {query}")

    page.keyboard.press("Enter")

    page.wait_for_timeout(10000)

    print("Search completed.")

    return p, browser, page


def get_business_links(page):

    links = page.get_by_role("link").all()

    businesses = []
    seen_urls = set()

    for link in links:

        try:

            href = link.get_attribute("href")

            if not href:
                continue

            if "/maps/place/" not in href:
                continue

            if href in seen_urls:
                continue

            seen_urls.add(href)

            business_name = (
                href.split("/place/")[1]
                .split("/data")[0]
            )

            business_name = unquote(
                business_name
            ).replace("+", " ")

            businesses.append({
                "name": business_name,
                "url": href
            })

        except Exception:
            continue

    return businesses


def scrape_business_details(page, business):

    page.goto(
        business["url"],
        timeout=120000
    )

    page.wait_for_timeout(5000)

    address = ""
    phone = ""
    website = ""

    try:

        address_btn = page.locator(
            'button[aria-label^="Address:"]'
        ).first

        address = (
            address_btn.get_attribute(
                "aria-label"
            )
            .replace("Address: ", "")
            .strip()
        )

    except Exception:
        pass

    try:

        phone_btn = page.locator(
            'button[aria-label^="Phone:"]'
        ).first

        phone = (
            phone_btn.get_attribute(
                "aria-label"
            )
            .replace("Phone: ", "")
            .strip()
        )

    except Exception:
        pass

    try:

        website_link = page.locator(
            'a[aria-label^="Website:"]'
        ).first

        website = website_link.get_attribute(
            "href"
        )

        if website:
            website = website.strip()

    except Exception:
        pass

    return {
        "place_id": extract_place_id(
            business["url"]
        ),
        "name": business["name"],
        "address": address,
        "phone": phone,
        "website": website,
        "maps_url": business["url"]
    }