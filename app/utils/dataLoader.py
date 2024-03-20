from .constants import CSV_FILES
import pandas as pd
import logging
from pathlib import Path
from app.models.card_status import db, PickedUp, Delivered, DeliveryException, Returned
from .dataCleaner import clean_phone_numbers, parse_dates
from .errorHandler import error_handler

logger = logging.getLogger(__name__)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
print(PROJECT_ROOT)


@error_handler(rollback_db=True)
def process_csv_file(file_path, model, phone_column):
    df = pd.read_csv(file_path)
    # Trim whitespace from column headers and standardize phone numbers
    df.columns = df.columns.str.strip()
    df = clean_phone_numbers(df, phone_column)
    df = parse_dates(df, 'Timestamp')

    for _, row in df.iterrows():
        timestamp = row['Timestamp'] if isinstance(row['Timestamp'], str) else row['Timestamp'].strftime(
            '%Y-%m-%d %H:%M:%S')
        record = model(
            id=row.get('ID', None),
            card_id=row['Card ID'],
            phone_number=row[phone_column],
            timestamp=timestamp,
            comments=row.get('Comment', '')
        )
        db.session.add(record)
    db.session.commit()


@error_handler()
def load_csv_data_into_db(models_to_load):
    model_mapping = {
        'picked_up': PickedUp,
        'delivered': Delivered,
        'delivery_exception': DeliveryException,
        'returned': Returned,
    }

    logger.debug("Starting to load CSV data into the database.")

    for status_type, model in model_mapping.items():
        if model not in models_to_load:
            continue

        filename = CSV_FILES.get(status_type)
        if not filename:
            logger.error(f"Filename for status type {status_type} not found.")
            continue

        file_path = PROJECT_ROOT / filename
        logger.debug(f"Processing {filename} for status type {status_type}.")
        phone_column = 'User Mobile' if 'User Mobile' in pd.read_csv(file_path, nrows=1).columns else 'User contact'
        process_csv_file(file_path, model, phone_column)

    logger.debug("Completed loading CSV data into the database.")
