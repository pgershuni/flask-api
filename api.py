from flask import jsonify
from flask.blueprints import Blueprint


class Job:

    def __init__(self, worker, duration, salary, discription):
        self.worker = worker
        self.duration = duration
        self.salary = salary
        self.discription = discription

    def to_dict(self):
        return {'worker': self.worker, 'duration': self.duration,
                'saary': self.salary, 'discription': self.discription}


jobs = [
    Job('Misha', 60, 1000, 'Nothing'),
    Job('Pavel', 60, 500, 'Nothing'),
    Job('Svyatislav', 60, 1e6, 'Nothing'),
]


api = Blueprint('api', __name__)

@api.route('/api/jobs', methods=['GET'])
def get_job():
    return jsonify(
        {
            'jobs': [job.to_dict() for job in jobs]
        }

    )
