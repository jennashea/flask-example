from flask import Flask
#for flashier front end: import render_template

app = Flask(__name__)


@app.route('/')
def health_check():
    return "hello, world"

@app.route('/<int:number>')
def display_integers(number):
    numbers = [str(x) for x in range(1,number+1)]
    return ", ".join(numbers)

@app.route('/<int:number>/odd')
def display_odds(number):
    numbers = [str(x) for x in range(1,number+1,2)]
    return ", ".join(numbers)

@app.route('/<int:number>/even')
def display_evens(number):
    numbers = [str(x) for x in range(2,number+1,2)]
    return ""

@app.route('/<int:number>/prime')
def display_primes(number):
    return ""
