from flask import Flask, jsonify
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)

r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/api')
def api():

    counter = r.incr("counter")

    return jsonify({
        "message": "Backend raggiunto correttamente",
        "service": "Redis raggiunto correttamente",
        "counter": counter
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)