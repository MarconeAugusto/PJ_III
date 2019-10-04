# import sys
# print(sys.path)
from flask import Flask, Blueprint
from flask_cors import CORS
from apirest.api_usuario import bp_usuario
from apirest.api_vaga import bp_vaga


# app = App('app', __name__)
app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "SO_SECURE"

app.register_blueprint(bp_usuario)
app.register_blueprint(bp_vaga)