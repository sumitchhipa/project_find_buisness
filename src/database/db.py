import sqlite3
from pathlib import Path

DB_PATH = Path("data/businesses.db")


def get_connection():
    return sqlite3.connect(DB_PATH)


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS businesses (

            place_id TEXT PRIMARY KEY,

            name TEXT NOT NULL,

            address TEXT,
            category TEXT,
            phone TEXT,
            website TEXT,
            maps_url TEXT,

            first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def business_exists(place_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT 1
        FROM businesses
        WHERE place_id = ?
        """,
        (place_id,)
    )

    result = cursor.fetchone()

    conn.close()

    return result is not None


def save_business(business):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO businesses (

            place_id,
            name,
            address,
            category,
            phone,
            website,
            maps_url

        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (

        business["place_id"],
        business["name"],
        business.get("address", ""),
        business.get("category", ""),
        business.get("phone", ""),
        business.get("website", ""),
        business.get("maps_url", "")

    ))

    conn.commit()
    conn.close()


def get_all_place_ids():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT place_id FROM businesses"
    )

    results = cursor.fetchall()

    conn.close()

    return {row[0] for row in results}


def get_total_businesses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM businesses"
    )

    total = cursor.fetchone()[0]

    conn.close()

    return total