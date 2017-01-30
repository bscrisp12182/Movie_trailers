import media
import fresh_tomatoes

#populate the class with the required info (name, summary, poster, trailer url, imdb url)
inception=media.Movie("Inception",
                      "A movie about a dream within a dream within a dream",
                      "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", # noqa
                      "https://www.youtube.com/watch?v=66TuSJo4dZM",
                      "http://www.imdb.com/title/tt1375666/?ref_=fn_al_tt_1")

matrix=media.Movie("Matrix",
                   "Neo versus the 'agents' in the fight to save humanity"+
                   "from the machines",
                   "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                   "https://www.youtube.com/watch?v=m8e-FF8MsqU",
                   "http://www.imdb.com/title/tt0133093/?ref_=fn_al_tt_1")

looper=media.Movie("Looper",
                   "The mob sends people back in time to murder but once your"+
                   "contract is up the loop must be closed",
                   "https://upload.wikimedia.org/wikipedia/en/0/0a/Looper_poster.jpg", # noqa
                   "https://www.youtube.com/watch?v=2iQuhsmtfHw",
                   "http://www.imdb.com/title/tt1276104/?ref_=fn_al_tt_1")

guardians_of_the_galaxy=media.Movie("Guardians of the Galaxy",
                                    "Star-Lord must team up with a group of "+
                                    "misfits to save the universe",
                                    "https://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg", # noqa
                                    "https://www.youtube.com/watch?v=B16Bo47KS2g", # noqa
                                    "http://www.imdb.com/title/tt2015381/?ref_=nv_sr_2") # noqa

anchorman=media.Movie("Anchorman",
                      "Ron Burgandy is the top anchorman in San Diego in the" +
                      " 1970s until Veronica Corningstone shakes up his world",
                      "https://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg", # noqa
                      "https://www.youtube.com/watch?v=Ip6GolC7Mk0",
                      "http://www.imdb.com/title/tt0357413/?ref_=nv_sr_2")


                
movies = [ inception, matrix, looper, guardians_of_the_galaxy, anchorman ]
print media.Movie.__init__.__doc__
fresh_tomatoes.open_movies_page(movies)
