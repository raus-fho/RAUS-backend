from flask import Flask

app = Flask(__name__)

from app.api import routes

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')