from flask import Flask, jsonify
from sympy import isprime

app = Flask(__name__)

airport_data = {
    "EFHK": {"Name": "Helsinki-Vantaa Airport", "Location": "Helsinki"},
    "KJFK": {"Name": "John F. Kennedy International Airport", "Location": "New York"},
    "EGLL": {"Name": "Heathrow Airport", "Location": "London"},

}

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to the Flask API! Use /prime_number/<number> or /airport/<icao> to access information."})

@app.route('/prime_number/<int:number>', methods=['GET'])
def check_prime(number):
    """Check if a number is prime."""
    result = {
        "Number": number,
        "isPrime": isprime(number)
    }
    return jsonify(result)

@app.route('/airport/<icao>', methods=['GET'])
def get_airport_info(icao):

    airport = airport_data.get(icao)
    if airport:
        result = {
            "ICAO": icao,
            "Name": airport["Name"],
            "Location": airport["Location"]
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)