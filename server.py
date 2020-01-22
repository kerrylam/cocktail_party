from flask import Flask, render_template, request

from pprint import pformat
import os
import requests

app = Flask(__name__)
app.secret_key = 'YUMMY'

@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')

@app.route('/cocktail/search')
def find_cocktails():
    """Search for cocktails on The Cocktail DB."""

    keyword = request.args.get('keyword', '')

    url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php'
    response = requests.get(url, params= {'s': keyword})
    data = response.json()
    cocktails = data['drinks']

    return render_template('cocktail-search-results.html',
                            pformat=pformat,
                            data=data,
                            results=cocktails)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')