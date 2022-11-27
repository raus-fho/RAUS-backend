from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

from app.api import routes

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')