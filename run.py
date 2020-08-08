from flask import Flask
from api.runScript.main import run
app = Flask(__name__)


app.register_blueprint(run)


if __name__ == '__main__':
    app.run(debug=True)
