from flask import Flask, jsonify
import requests
from config import SLAVES

app = Flask(__name__)


@app.route('/all_resources')
def all_resources():
    all_data = {}
    for i, slave in enumerate(SLAVES):
        try:
            response = requests.get(slave)
            if response.status_code == 200:
                all_data[f"raspberry_{i+1}"] = response.json()
            else:
                all_data[f"raspberry_{i+1}"] = "Erreur de récupération des données"
        except requests.exceptions.RequestException:
            all_data[f"raspberry_{i+1}"] = "Inaccessible"

    return jsonify(all_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=True)
