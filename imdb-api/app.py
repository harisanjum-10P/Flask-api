import urllib.request, json
from flask import *
import os

app = Flask(__name__)

url = "https://api.themoviedb.org/3/discover/movie?api_key=383c69c445a16c97415a236f430ee2ae"
response = urllib.request.urlopen(url)
data = response.read()
dict = json.loads(data)

@app.route("/")
def get_movies():

    print(dict)

    return render_template ("movies.html", movies=dict["results"])



@app.route("/moviesList")
def get_movies_list():

    movies = []

    for movie in dict["results"]:
        movie = {
            "title": movie["title"],
            "overview": movie["overview"],
        }
        
        movies.append(movie)

    return {"results": movies}




@app.route('/resultMovie/<name>')
def resultMovie(name):

   for movie in dict['results']:
        if movie['original_title']==name:
            finalMovie=movie
            break
        else:
            finalMovie="Nothing"


   return render_template('movie_choice_result.html',movie=finalMovie)

@app.route('/abc',methods = ['POST', 'GET'])
def abc():
   if request.method == 'POST':
      selectedMovie = request.form['movieName']
      return redirect(url_for('resultMovie',name = selectedMovie))
   else:
      user = request.args.get('movieName')
      return redirect(url_for('resultMovie',name = selectedMovie))
   

@app.route('/wantMyMovie')
def wantMyMovie():

    return render_template('movie_choice.html', allMovies=dict['results'])
   


if __name__ == '__main__':
    app.run(debug=True)

