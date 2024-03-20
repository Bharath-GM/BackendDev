CSV_FILES = {
    'picked_up': 'data/Sample Card Status Info - Pickup.csv',
    'delivered': 'data/Sample Card Status Info - Delivered.csv',
    'delivery_exception': 'data/Sample Card Status Info - Delivery exceptions.csv',
    'returned': 'data/Sample Card Status Info - Returned.csv',
}

header_mapping = {
    'User contact': 'User contact',
    'User Mobile': 'User contact',
    'Comment': 'Comment',
    'ID': 'ID',
    'Card ID': 'Card ID',
    'Timestamp': 'Timestamp'
    # Add more mappings as needed
}

date_formats = [
    "%d-%m-%Y %I:%M%p",  # Example: 14-11-2023 12:00PM
    "%d-%m-%Y %H:%M %p",  # Example: 12-11-2023 11:59 PM (with space before AM/PM)
    "%d-%m-%Y %H:%M",  # Example: 13-11-2023 14:00
    "%Y-%m-%dT%H:%M:%SZ",  # Example: 2023-11-13T09:34:56Z
    # Add more formats as needed
]