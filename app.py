from flask import Flask
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello'

@app.route('/mi')
def michigan():
    data = []
    with open('./mi.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            split = row[3].split('(')
            try:
                [lat, long] = split[1].split(' ')
                data.append({
                    "rate": row[2],
                    "point": {
                        "latitude": lat,
                        "longitude": long[:len(long)-1]
                    }
                })
            except:
                print("ERROR")
    return data

if __name__ == '__main__':
    app.run(debug=True)