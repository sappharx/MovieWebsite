"""
This module defines the movie objects that are to displayed on the webpage.
It also uses the fresh_tomatoes module to generate the webpage and launch it in a browser.
"""

import fresh_tomatoes
import media

def main():
    """
    Creates the movies, renders the html for the webpage, and displays the page
    """

    # create movie objects
    holy_grail = media.Movie("Monty Python and the Holy Grail",
                             "King Arthur and his knights search for the holy grail",
                             "https://upload.wikimedia.org/wikipedia/en/4/49/Monty_python_and_the_holy_grail_2001_release_movie_poster.jpg",
                             "https://www.youtube.com/watch?v=hKNDml12Big")

    from_hell = media.Movie("From Hell",
                            "In Victorian Era London, a troubled clairvoyant police detective investigates the murders by Jack the Ripper",
                            "https://upload.wikimedia.org/wikipedia/en/6/66/From_Hell_film.jpg",
                            "https://www.youtube.com/watch?v=EpOwhXPhPQ8")

    minority_report = media.Movie("Minority Report",
                                  "For six years, Washington, D.C. has been murder free thanks to astounding technology which identifies killers before they commit their crime",
                                  "https://upload.wikimedia.org/wikipedia/en/4/44/Minority_Report_Poster.jpg",
                                  "https://www.youtube.com/watch?v=jdl6eAIx2K4")

    american_psycho = media.Movie("American Psycho",
                                  "Patrick Bateman is a Wall Street yuppie, obsessed with success, status, and style, with a stunning fiancee",
                                  "https://upload.wikimedia.org/wikipedia/en/6/63/Americanpsychoposter.jpg",
                                  "https://www.youtube.com/watch?v=5YnGhW4UEhc")

    pulp_fiction = media.Movie("Pulp Fiction",
                               "Hit men, gansters, and robbers converge in Quentin Tarantino's violent tale of revenge",
                               "https://upload.wikimedia.org/wikipedia/en/8/82/Pulp_Fiction_cover.jpg",
                               "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

    house_of_flying_daggers = media.Movie("House of Flying Daggers",
                                          "In 859 CE, the once great Tang Dynasty is in decline.  Numerous rebel groups have formed, the largest of which is the House of Flying Daggers",
                                          "https://upload.wikimedia.org/wikipedia/en/f/f7/House_of_Flying_Daggers_poster.JPG",
                                          "https://www.youtube.com/watch?v=ZUyFAlIJgLA")

    # put movie objects into list (to pass into rendering function)
    movies = [holy_grail, from_hell, minority_report, american_psycho, pulp_fiction, house_of_flying_daggers]

    # generate html page and open in browser
    fresh_tomatoes.open_movies_page(movies)

# check if running as program
if __name__ == '__main__':
    main()
