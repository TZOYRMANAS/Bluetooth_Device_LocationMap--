from flask import Flask, render_template, jsonify

app = Flask(__name__)

json_data = [
        {
                    "id":" B8:90:47:90:80:AF",
                    "reportTime":" 2023-07-28T14:43:13.478702",
                    "location": {
                        "latitude": 40.6436,
                        "longitude": 22.9309
                    },
                    "sensorName":" Eftihia\u2019s iPhone",
                    "sensorStatus": "string",
                    "imei": "string",
                    "email": "string",
                    "mobileId": "string",
                    "category": "string",
                    "reportAction": 0,
                    "message": "string",
                    "isPerson": True
            }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    return jsonify(json_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
