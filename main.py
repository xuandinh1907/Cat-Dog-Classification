from flask import Flask, render_template , send_from_directory
from blueprints import *

app = Flask(__name__)
app.register_blueprint(home)
app.register_blueprint(classify)
app.register_blueprint(retrain)

UPLOAD_FOLDER = 'uploads'

@app.route('/classify/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 