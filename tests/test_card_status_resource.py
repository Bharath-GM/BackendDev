from datetime import datetime
import unittest
from flask import current_app
from app import create_app, db
from app.models.card_status import PickedUp, Delivered, DeliveryException, Returned
from tests.conftest import TestConfig

class CardStatusResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

        # Insert test entries for each status type
        statuses = [
            PickedUp(id='1', card_id='123', phone_number='555000111', timestamp=datetime.now(), comments='Picked up'),
            Delivered(id='2', card_id='124', phone_number='555000112', timestamp=datetime.now(), comments='Delivered'),
            DeliveryException(id='3', card_id='125', phone_number='555000113', timestamp=datetime.now(), comments='Delivery exception'),
            Returned(id='4', card_id='126', phone_number='555000114', timestamp=datetime.now(), comments='Returned')
        ]
        db.session.bulk_save_objects(statuses)
        db.session.commit()

        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_get_card_status(self):
        # Test retrieving each status by card_id
        for status in ['PickedUp', 'Delivered', 'DeliveryException', 'Returned']:
            with self.subTest(status=status):
                response = self.client.get(f'/get_card_status?identifier=12{status[-1]}')  # Assuming URL and query param
                self.assertEqual(response.status_code, 200)
                data = response.get_json()
                self.assertIsNotNone(data)
                self.assertEqual(data['status'], status.lower())  # Assuming response includes 'status' field



if __name__ == '__main__':
    unittest.main()