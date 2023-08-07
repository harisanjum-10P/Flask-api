import urllib.request, json
from flask import *
import os
import requests

app = Flask(__name__)

@app.route('/getJoke/<category>')
def getJoke(category):
    full_url = 'https://api.chucknorris.io/jokes/random?category={}'.format(category)

    response = requests.get(full_url)
    if response.status_code == 200:
        joke_data = response.json()
    else:
        joke_data='No Joke'
   
    return render_template('index.html', jokes=joke_data)


@app.route('/joke',methods = ['POST', 'GET'])
def joke():
   if request.method == 'POST':
      selectedCategory = request.form['ctg']
      return redirect(url_for('getJoke',category = selectedCategory.strip().lower()))
   else:
      selectedCategory = request.args.get('ctg')
      return redirect(url_for('getJoke',category = selectedCategory.strip().lower()))


@app.route('/')
def index():

    full_url = 'https://api.chucknorris.io/jokes/categories'
    response = requests.get(full_url)
    if response.status_code == 200:
        categories = response.json()
    else:
        categories='No Joke'

    return render_template('category.html', categories=categories)



if __name__ == '__main__':
    app.run(debug=True)