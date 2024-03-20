import re
from .constants import date_formats
from datetime import datetime
import pandas as pd
import logging
logger = logging.getLogger(__name__)



def clean_phone_numbers(df, column_name):
    """
    Cleans and standardizes phone numbers in the specified column of a DataFrame.
    Removes non-digit characters and trims the first three characters if it starts with '971'.

    Parameters:
    - df: pandas DataFrame containing the data.
    - column_name: The name of the column with phone numbers to clean.

    Returns:
    - The DataFrame with cleaned and standardized phone numbers.
    """

    pattern = re.compile(r'\D')  # Matches any non-digit character

    def clean_number(number):
        try:
            # Remove non-digit characters
            cleaned_number = re.sub(pattern, '', number)
            return cleaned_number
        except Exception as e:
            logger.error(f"Error cleaning phone number {number}: {e}")
            return number  # Return the original number in case of an error

    try:
        df[column_name] = df[column_name].astype(str).apply(clean_number)
    except Exception as e:
        logger.error(f"Error processing phone numbers in column {column_name}: {e}")

    return df





def parse_dates(df, column_name):
    """
    Convert all dates in the specified column of a DataFrame to datetime64 format,
    trying multiple formats and falling back to pd.to_datetime for unrecognized formats.

    Parameters:
    - df: DataFrame containing the column with dates.
    - column_name: Name of the column with date strings to convert.
    Returns:
    - DataFrame with the specified column converted to datetime64 format.
    """


    def try_parse_date(date_str):
        for fmt in date_formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        try:
            # If none of the formats work, fall back to pd.to_datetime
            return pd.to_datetime(date_str, errors='coerce', utc=True)
        except Exception as fallback_error:
            logger.error(f"Error parsing date {date_str}: {fallback_error}")
            return pd.NaT

    try:
        df[column_name] = df[column_name].apply(lambda x: try_parse_date(str(x)))
    except Exception as e:
        logger.error(f"Error processing dates in column {column_name}: {e}")

    return df