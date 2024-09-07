from flask import Flask
from flask_cors import CORS, cross_origin
import csv

app = Flask(__name__)
CORS(app, origins=['http://localhost:5713/'])

@app.route('/')
@cross_origin()
def index():
    return 'Hello'

@app.route('/mi')
@cross_origin()
def michigan():
    data = []
    with open('./mi.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            split = row[3].split('(')
            try:
                [lat, long] = split[1].split(' ')
                if len(data) < 1000:
                    data.append({
                        "rate": row[2],
                        "coordinates": [lat, long[:len(long)-1]]
                    })
            except:
                print("ERROR")
    return data

if __name__ == '__main__':
    app.run(debug=True)