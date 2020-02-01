from flask import Flask, render_template, request, flash, redirect, session
from model import connect_to_db, db, User, Liquor, Cocktail
import api
import requests


app = Flask(__name__)
app.secret_key = 'YUMMY'

@app.route('/')
def homepage():
    """Show homepage."""

    cocktail_ids = (11000, 11001, 11002, 11003, 11004, 11005, 11006, 11007,\
                    11008, 11009)
    url = 'https://www.thecocktaildb.com/api/json/v1/1/lookup.php'
    results = []
    for cocktail_id in cocktail_ids:
        response = requests.get(url, params= {'i': cocktail_id})
        data = response.json()
        cocktail = data['drinks']
        results.append(cocktail)

    return render_template('homepage.html',
                           results=results)


@app.route('/register', methods=['GET'])
def register_user():
    """Show registration form.

    Get user first and last name, email, username, & password.
    """

    return render_template("register.html")


@app.route('/handle_registration_form', methods=['POST'])
def handle_registration_form():
    """Handle registration form submission."""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")

    if User.query.filter_by(email=email).first():
        flash('Email address already exists, please enter a different email.')
        return redirect("/register")
    elif User.query.filter_by(username=username).first():
        flash('Username taken, please enter a different username.')
        return redirect("/register")
    else:
        new_user = User(fname=fname, lname=lname, username=username,
                        email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash(f'Hi {fname}! Welcome to Cocktail Party.')
        return redirect('/')


@app.route('/login', methods=['GET'])
def login():
    """User login form."""

    return render_template('login.html')


@app.route('/login', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')
    login_user = User.query.filter_by(username=username).first()
    if login_user:
        if login_user.password == password:
            session['user_id'] = login_user.user_id
            flash(f'Hi {login_user.fname}!')
            return redirect("/")
        else:
            flash('Incorrect password')
            return redirect('/login')
    else:
        flash('Invalid username.')
        return redirect('/login')


# @app.route('/cocktail/<cocktail_id>')
# def show_cocktail_details(cocktail_id):
#     """Show cocktail details

#     list of ingredients, measurements, and instructions.
#     """

#     url = 'https://www.thecocktaildb.com/api/json/v1/1/lookup.php'
#     response = requests.get(url, params= {'i': cocktail_id})
#     data = response.json()
#     result = data['drinks']
#     for cocktail in result:





@app.route('/cocktail/search')
def find_cocktails():
    """Search for cocktails on The Cocktail DB."""

    keyword = request.args.get('keyword', '')

    url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php'
    response = requests.get(url, params= {'s': keyword})
    data = response.json()
    cocktails = data['drinks']

    return render_template('cocktail-search-results.html',
                            results=cocktails)


if __name__ == '__main__':
    app.debug = True
    connect_to_db(app)
    app.run(host='0.0.0.0')