from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "jgakwenkn4nan4"
from app import routes