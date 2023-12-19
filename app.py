from flask import Flask, request
from flask_restful import Api, Resource
import pandas as pd

app = Flask(__name__)
api = Api(app)
        
class Users(Resource):
    def get(self):
        data = pd.read_csv('info.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200

    def post(self):
        name = request.args['name']
        age = request.args['age']
        city = request.args['city']
        req_data = pd.DataFrame({
            'name'      : [name],
            'age'       : [age],
            'city'      : [city]
        })
        data = pd.read_csv('info.csv')
        data = data.append(req_data, ignore_index=True)
        data.to_csv('info.csv', index=False)
        return {'message' : 'Kayit basariyla eklendi.'}, 200

class Name(Resource):
    def get(self,name):
        data = pd.read_csv('info.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['name'] == name :
                return {'data' : entry}, 200
        return {'message' : 'No entry found with this name !'}, 404



api.add_resource(Users, '/users')
api.add_resource(Name, '/isim/<string:name>')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
    app.run()
