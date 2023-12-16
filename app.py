from flask import Flask
from flask_restful import Api, Resource, reqparse
import pandas as pd

app = Flask(__name__)
api = Api(app)

class Quotes(Resource):
    def get(self):
        data = pd.read_csv('quotes.csv')
        data = data.to_dict('records')
        return {'data' : data}, 200

    def post(self):
        date = request.args['date']
        quotes = request.args['quotes']
        theme = request.args['theme']

        data = pd.read_csv('quotes.csv')

        new_data = pd.DataFrame({
            'date': [date],
            'quotes': [quotes],
            'theme': [theme]
        })
        data = data.append(new_data, ignore_index=True)
        data.to_csv('quotes.csv', index=False)
        return {'data': new_data.to_dict('records')}, 200

class Date(Resource):
    def get(self, date):
        data = pd.read_csv('quotes.csv')
        data = data.to_dict('records')
        
        matching_entries = []
        for entry in data:
            # Karşılaştırma yaparken tür uyumsuzluğu önlemek için str() kullan
            if entry['date'] == date:
                matching_entries.append(entry)
        
        if matching_entries:
            return {'data': matching_entries}, 200
        else:
            return {'message': 'Girilen tarihte bir soz bulunamadi !'}, 404


# Add URL endpoints
api.add_resource(Quotes, '/quotes')
api.add_resource(Date, '/date/<int:date>')

if __name__ == '__main__':
    app.run(host="0.0.0.0")
    app.run()

