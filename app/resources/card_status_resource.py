from flask_restx import Resource, Namespace, reqparse
from app.services.card_status_service import CardStatusService
import logging


api = Namespace('card_status', description='Card Status operations')



parser = reqparse.RequestParser()
parser.add_argument('identifier', required=True, help="Card ID or User's Phone Number")


@api.errorhandler(Exception)
def handle_exception(error):
    logging.error(f"Unhandled exception: {error}")
    return {'message': 'An internal error occurred'}, 500




@api.route('/get_card_status')
class CardStatusResource(Resource):
    @api.expect(parser)
    def get(self):
        args = parser.parse_args()
        identifier = args['identifier']

        # Use the updated service function to get the latest status
        latest_status = CardStatusService.fetch_card_status_latest(identifier)

        if latest_status:
            # Format the response based on your service's return value
            return {
                'timestamp': latest_status.get('timestamp'),
                'comment': latest_status.get('comments'),
                'status': latest_status.get('status')
            }, 200

        # If no status is found, return a 404 response
        api.abort(404, 'Card status not found')
