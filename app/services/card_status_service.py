import logging
import re
from app.models.card_status import db, PickedUp, Delivered, DeliveryException, Returned
from ..utils.errorHandler import error_handler

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class CardStatusService:

    @staticmethod
    @error_handler(rollback_db=False)
    def fetch_card_status_latest(identifier):
        models = [PickedUp, Delivered, DeliveryException, Returned]
        all_statuses = []

        # Determine if identifier is a phone number using regular expression
        if re.match(r'^\+?\d{9,12}$', identifier):
            # If identifier is a phone number, take the last 9 digits
            phone_number_identifier = identifier[-9:]
        else:
            # Otherwise, use the identifier as-is
            phone_number_identifier = identifier

        for model in models:
            result = db.session.query(
                model.card_id, model.phone_number, model.timestamp, model.comments,
                db.literal(f'{model.__tablename__}').label('status')
            ).filter(
                (model.card_id == identifier) |
                # Use phone_number_identifier for phone number related query
                (model.phone_number.endswith(phone_number_identifier))
            ).all()

            all_statuses.extend(result)
            logger.debug(f"result for model {model}: {result}")

        if all_statuses:
            # Sort all statuses by timestamp
            all_statuses.sort(key=lambda x: x.timestamp, reverse=True)
            logger.debug(f"Sorted all_statuses: {all_statuses}")
            latest_status = all_statuses[0]

            return {
                'timestamp': latest_status.timestamp.isoformat(),
                'comments': latest_status.comments,
                'status': latest_status.status
            }

        logger.debug("No status found for the given identifier.")
        return None




