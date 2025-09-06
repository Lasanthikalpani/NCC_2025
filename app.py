﻿from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Docker! GSC0MP334 application is running successfully!'

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'Docker deployment working'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
