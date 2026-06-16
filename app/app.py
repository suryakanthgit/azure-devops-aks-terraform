from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>System Health Dashboard</h1>
    <p>Status: <span style="color:green">UP</span></p>
    <p>Time: ''' + str(datetime.now()) + '''</p>
    '''

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "time": str(datetime.now())
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)