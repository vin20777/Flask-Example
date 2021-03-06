from flask import Flask
from controllers import homeController, moviesController, movieController, addMovieController, editMovieController
from database import Database
from models.movie import Movie

def create_app():
    app = Flask(__name__)
    app.config.from_object("settings")

    app.add_url_rule("/", view_func=homeController.home_page)
    app.add_url_rule("/movies", view_func=moviesController.movies_page, methods=["GET", "POST"])
    app.add_url_rule("/movies/<int:movie_key>", view_func=movieController.detail_page)
    app.add_url_rule("/new-movie", view_func=addMovieController.movie_add_page, methods=["GET", "POST"])
    app.add_url_rule("/movies/<int:movie_key>/edit", view_func=editMovieController.movie_edit_page, methods=["GET", "POST"])

    createMockUpDB(app=app)

    return app

def createMockUpDB(app):
    db = Database()
    db.add_movie(Movie("Slaughterhouse-Five", year=1972))
    db.add_movie(Movie("The Shining"))
    db.add_movie(Movie("絕命終結站2", year=2020))
    app.config["db"] = db

if __name__ == "__main__":
    app = create_app()
    port = app.config.get("PORT", 5000)
    app.run(host="0.0.0.0", port=port)
