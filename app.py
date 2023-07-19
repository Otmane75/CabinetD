from flask import Flask
import scripts.gestionDB as db
from flask_restful import Api
from flask_restful import Resource,reqparse

import json

app = Flask(__name__)
api = Api(app)



class getOper(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('param', type=str, required=True)
        super(getOper, self).__init__()

    def get(self):
        operations = db.lire_operations()
        return operations

    def post(self):
        args = self.parser.parse_args()
        arg1 = args['param']
        certificat=db.lire_certificat(int(arg1))
        # Logique pour créer un nouvel utilisateur
        #return {'user_id': param, 'name': 'John Doe'}
        return certificat
api.add_resource(getOper, '/operations', '/operations/<int:param>')


if __name__ == '__main__':
    app.run()