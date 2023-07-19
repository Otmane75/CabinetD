from flask import Flask
import scripts.gestionDB as db
from flask_restful import Api
from flask_restful import Resource,reqparse

from datetime import datetime

import json

app = Flask(__name__)
api = Api(app)



class getOper(Resource):
    
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('nom', type=str, required=True)
        self.parser.add_argument('prenom', type=str, required=True)
        self.parser.add_argument('telphone', type=str, required=True)
        self.parser.add_argument('operation', type=str, required=True)
        self.parser.add_argument('prix', type=float, required=True)
        self.parser.add_argument('paye', type=float, required=True)
        self.parser.add_argument('date', type=str, required=True)
        super(getOper, self).__init__()

    def get(self):
        operations = db.lire_operations()
        return operations

    def post(self):
        args = self.parser.parse_args()
        arg1 = args['nom']
        arg2 = args['prenom']
        arg3 = args['telphone']
        arg4 = args['operation']
        arg5 = args['prix']
        arg6 = args['paye']
        arg7 = args['date']
        format_string = "%Y-%m-%d"  # Format of the date string, e.g., "YYYY-MM-DD"
        date_object = datetime.strptime(arg7, format_string)
        if db.ajouter_operation(arg1,arg2,arg3,arg4,arg5,arg6,date_object):
            return "done"
        else:
            return "erreur d ajout"
        # Logique pour créer un nouvel utilisateur
        #return {'user_id': param, 'name': 'John Doe'}
        
api.add_resource(getOper, '/operations', '/operations/<int:param>')


if __name__ == '__main__':
    app.run()