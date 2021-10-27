# from flask import render_template
from app import app
from modules.calculator import *

@app.route('/')
def index():
    return "Welcome to the calculator"

@app.route('/add/<num1>/<num2>')
def addition(num1, num2):
    return f'{add(int(num1), int(num2))}'



