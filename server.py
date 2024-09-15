from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Good format
# start long, lon
# end long, lat

@app.route("/route", methods=['POST'])
def getRoute():
    data = request.get_json()
    if request.method == 'POST':
        return computeRoute((input["start_lat"], input["start_long"]), (input["start_lat"], input["start_long"]))
    return "Please use a POST request"  


@app.route("/accel", methods=['POST'])
def get_acceleration():
    data = request.get_json()
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return jsonify({"status": "Acceleration data saved"}), 200


def computeRoute(startCoordinates, endCoordinates):
    return jsonify({"status": "Rcout"}), 200


if __name__ == "__main__":
    app.run()
