import datetime
import socket

from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/api/v1/details')

def details():
    return jsonify({
        'time': datetime.datetime.now().isoformat(),
        'host': socket.gethostname(),
        'message': "ahhh!!"
    })


@app.route('/api/v1/health')
def health():
    return jsonify({'status': ' Up'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)