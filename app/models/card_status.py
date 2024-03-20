from app.extensions import db



class BaseStatus(db.Model):
    __abstract__ = True

    id = db.Column(db.String(120),primary_key=True)
    card_id = db.Column(db.String(120), unique=False, nullable=False)
    phone_number = db.Column(db.String(12), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    comments = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<PickedUp(id={self.id}, card_id='{self.card_id}', phone_number='{self.phone_number}', timestamp='{self.timestamp}', comments='{self.comments}')>"



class PickedUp(BaseStatus):
    __tablename__ = 'picked_up'

class Delivered(BaseStatus):
    __tablename__ = 'delivered'

class DeliveryException(BaseStatus):
    __tablename__ = 'delivery_exception'

class Returned(BaseStatus):
    __tablename__ = 'returned'