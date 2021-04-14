from app import app
from modules.calculator import *

@app.route("/")
def index():
    return "Please enjoy this humble calculator."

@app.route("/add/<number_1>/<number_2>")
def add_from_url(number_1, number_2):
    number_1 = int(number_1)
    number_2 = int(number_2)
    return add(number_1, number_2)

@app.route("/subtract/<number_1>/<number_2>")
def subtract_from_url(number_1, number_2):
    number_1 = int(number_1)
    number_2 = int(number_2)
    return subtract(number_1, number_2)

@app.route("/multiply/<number_1>/<number_2>")
def multiply_from_url(number_1, number_2):
    number_1 = int(number_1)
    number_2 = int(number_2)
    return multiply(number_1, number_2)

@app.route("/divide/<number_1>/<number_2>")
def divide_from_url(number_1, number_2):
    number_1 = int(number_1)
    number_2 = int(number_2)
    return divide(number_1, number_2)


