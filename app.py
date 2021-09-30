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
    return ", ".join(numbers)

@app.route('/<int:number>/prime')
def display_primes(number):
    #Sieve of Eratosthenes: effecient until number is > 10 mil
    prime = [True for x in range(number+1)]
    p = 2
    while p*p <= number:
        if prime[p]:
            for i in range(p*p, number+1, p):
                prime[i] = False
        p+=1

    numbers = []
    for x in range(2, number+1):
        if prime[x]:
            numbers.append(str(x))

    return ", ".join(numbers)
