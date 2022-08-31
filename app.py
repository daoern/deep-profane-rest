# rest api
from flask import Flask
from flask_restful import Resource, Api, reqparse

from deep_profane.validator import ProfanityValidator

app = Flask(__name__)
api = Api(app)

profane_checker = ProfanityValidator()

def get_msg():
    parser = reqparse.RequestParser()
    parser.add_argument('msg', action='append')
    args = parser.parse_args()
    return args['msg']

class IsProfane(Resource):
    def get(self):
        return {'is_profane': profane_checker.is_profane(get_msg()).tolist()}

class ProfaneProb(Resource):
    def get(self):
        return {'profane_prob':profane_checker.get_profane_prob(get_msg()).tolist()}

api.add_resource(IsProfane, '/is_profane')
api.add_resource(ProfaneProb, '/profane_prob')

if __name__ == '__main__': 
    app.run(debug=False, port=80)