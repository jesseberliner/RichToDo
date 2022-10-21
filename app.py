import ssl
import certifi
certifi_context = ssl.create_default_context(cafile=certifi.where())


from flask import Flask, render_template, request, redirect

import urllib.request, json
import os


app = Flask(__name__)

key="?api_key=042e5b31f2666180fed855ca8967674a"

@app.route("/")
def get_movies():
    print("/")
    url = "https://api.themoviedb.org/3/discover/movie" + key
    print(os.environ.get("TMDB_API_KEY"))
    response = urllib.request.urlopen(url, context=certifi_context)
    data = response.read()
    jsondata = json.loads(data)

    return render_template("movies.html", movies=jsondata["results"])

@app.route("/movies")
def get_movies_list():
    print("/movies")
    url = "https://api.themoviedb.org/3/movie/popular" + key
    print(os.environ.get("TMDB_API_KEY"))
    response = urllib.request.urlopen(url, context=certifi_context)
    data = response.read()
    jsondata = json.loads(data)

    movie_json = []

    for movie in jsondata["results"]:
        movie = {
            "title": movie["title"],
            # "overview": movie["overview"], this eliminates the massive wall of text to just movie titles
        }

        movie_json.append(movie)

    print(movie_json)

    return render_template("allmovies.html", titles=movie_json)

if __name__ == '__main__':
    app.run(debug=True)

app.run(host='localhost', port=5000)

#app.run(host='localhost', port=5000)
#https://www.youtube.com/watch?v=I0Zu-Jtp898
#https://github.com/geoffrey45/flask-request#readme
#https://www.section.io/engineering-education/integrating-external-apis-with-flask/
