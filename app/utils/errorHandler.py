from functools import wraps
import logging
logger = logging.getLogger(__name__)
from app.extensions import db


def error_handler(rollback_db=False):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.error(f"Error in {func.__name__}: {e}")
                if rollback_db:
                    db.session.rollback()

        return wrapper
    return decorator
