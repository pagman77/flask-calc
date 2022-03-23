from flask import Flask
from flask import request
from operations import OPERATIONS

app = Flask(__name__)

@app.get("/<operation>")
def calc(operation):
    """get operation information from request from server"""
    equation = OPERATIONS[operation]
    a = int(request.args["a"])
    b = int(request.args["b"])

    result = str(equation(a,b))

    return f"<html><body><h1>{result}</h1></body></html>"
