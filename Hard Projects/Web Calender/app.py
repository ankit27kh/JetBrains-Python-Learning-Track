import datetime
from flask import Flask, abort
import sys
from flask_restful import Api, Resource, reqparse, inputs
from flask_sqlalchemy import SQLAlchemy

# write your code here
app = Flask(__name__)
api = Api(app)
parser_for_post = reqparse.RequestParser()
parser_for_get = reqparse.RequestParser()
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'

parser_for_post.add_argument(
    'date',
    type=inputs.date,
    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
    required=True
)
parser_for_post.add_argument(
    'event',
    type=str,
    help="The event name is required!",
    required=True
)

parser_for_get.add_argument(
    'start_time',
    type=inputs.date,
    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
    required=False
)
parser_for_get.add_argument(
    'end_time',
    type=inputs.date,
    help="The event date with the correct format is required! The correct format is YYYY-MM-DD!",
    required=False
)


class EventByID(Resource):

    def get(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        return {
            'id': event.id,
            'event': event.event,
            'date': str(event.date)
        }

    def delete(self, event_id):
        event = Event.query.filter(Event.id == event_id).first()
        if event is None:
            abort(404, "The event doesn't exist!")
        db.session.delete(event)
        db.session.commit()
        return {"message": "The event has been deleted!"}


class Event(db.Model):
    __tablename__ = 'events_list'
    id = db.Column(db.Integer, primary_key=True)
    event = db.Column(db.String(80), nullable=False)
    date = db.Column(db.Date, nullable=False)


db.create_all()


class Hello(Resource):

    def get(self):
        return {'data': 'Hello'}


class EventsToday(Resource):

    def get(self):
        events = Event.query.filter(Event.date == datetime.date.today()).all()
        result = []
        for event in events:
            result.append({
                'id': event.id,
                'event': event.event,
                'date': str(event.date)
            })
        return result


class Events(Resource):

    def get(self):
        args = parser_for_get.parse_args()
        start = args['start_time']
        end = args['end_time']
        if start and end:
            events = Event.query.filter(start < Event.date).filter(Event.date < end).all()
        else:
            events = Event.query.all()
        result = []
        for event in events:
            result.append({
                'id': event.id,
                'event': event.event,
                'date': str(event.date)
            })
        return result

    def post(self):
        args = parser_for_post.parse_args()
        date = args['date']
        event_name = args['event']
        event = Event(event=event_name, date=date)
        db.session.add(event)
        db.session.commit()
        return {
            "message": "The event has been added!",
            "event": f"{event_name}",
            "date": f"{str(date.date())}"
        }


api.add_resource(EventByID, '/event/<int:event_id>')
api.add_resource(EventsToday, '/event/today')
api.add_resource(Events, '/event')
api.add_resource(Hello, '/')

# do not change the way you run the program
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()
