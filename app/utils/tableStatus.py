from app.models.card_status import PickedUp
from app.models.card_status import Delivered
from app.models.card_status import DeliveryException
from app.models.card_status import Returned
from app.extensions import db

import logging
from .errorHandler import error_handler
logger = logging.getLogger(__name__)
@error_handler(rollback_db=True)
def get_empty_tables():
    """Return a list of model classes for tables that are empty."""
    models = [PickedUp, Delivered, DeliveryException, Returned]
    empty_models = []

    for model in models:
        try:
            # Attempt to query the first row in the table
            if db.session.query(model).first() is None:  # Table is empty
                empty_models.append(model)
        except Exception as e:
            logger.error(f"Error querying {model.__tablename__}: {e}")


    return empty_models