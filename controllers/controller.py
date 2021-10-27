# from flask import render_template
from app import app
from modules.calculator import *

@app.route('/')
def index():
    return "Welcome to the calculator"

@app.route('/add/<num1>/<num2>')
def addition_route(num1, num2):
    return f'{add(int(num1), int(num2))}'

@app.route('/subtract/<num1>/<num2>')
def subtract_route(num1, num2):
    return f'{subtract(int(num1), int(num2))}'

@app.route('/multiply/<num1>/<num2>')
def multiply_route(num1, num2):
    return f'{multiply(int(num1), int(num2))}'

@app.route('/divide/<num1>/<num2>')
def divide_route(num1, num2):
    return f'{divide(int(num1), int(num2))}'




