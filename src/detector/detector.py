def find_new_businesses(current_businesses, existing_place_ids):
    """
    current_businesses -> list of businesses
    existing_place_ids -> set of place_ids from database
    """

    new_businesses = []

    for business in current_businesses:
        if business["place_id"] not in existing_place_ids:
            new_businesses.append(business)

    return new_businesses