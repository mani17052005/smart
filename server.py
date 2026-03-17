from flask import Flask, request, jsonify

app = Flask(__name__)

sensor_data = {
    "temperature": 0,
    "pressure": 0,
    "steps": 0,
    "glucose": 0
}

@app.route('/api/sensordata', methods=['POST'])
def receive_data():
    global sensor_data
    sensor_data = request.json
    return jsonify({"status": "received"})

@app.route('/api/latestdata', methods=['GET'])
def get_data():
    return jsonify(sensor_data)

if __name__ == "__main__":
    print("Server starting...")
    app.run(debug=True)