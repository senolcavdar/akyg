from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Says(Resource):
    def get(self):
        data = pd.read_csv('says.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200

    def post(self):
        date = request.args['date']
        says = request.args['says']
        topic = request.args['topic']

        data = pd.read_csv('says.csv')

        new_data = pd.DataFrame({
            'date': [date],
            'says': [says],
            'topic': [topic]
        })
        data = data.append(new_data, ignore_index=True)
        data.to_csv('says.csv', index=False)
        return {'data': new_data.to_dict('records')}, 200

class Date(Resource):
    def get(self, date):
        data = pd.read_csv('says.csv')
        data = data.to_dict('records')
        for entry in data:
            if entry['date'] == date:
                return {'data': entry}, 200
        return {'message': 'Girilen tarihte bir söz bulunamadı !'}, 404

# Add URL endpoints
api.add_resource(Says, '/says')
api.add_resource(Date, '/date/<string:date>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767)
    app.run()

