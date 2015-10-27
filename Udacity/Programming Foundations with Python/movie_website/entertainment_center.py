import fresh_tomatoes
import media

toy_story = media.Movie('Toy Story',						 
						 'https://upload.wikimedia.org/wikipedia/ru/a/a6/Toy_Story_1995_Poster.jpg',
						 'https://www.youtube.com/watch?v=KYz2wyBy3kc',
						 "A story of a boy and his toys that come to life")

avatar = media.Movie("Avatar",					 
					 'http://www.kinopoisk.ru/images/film_big/251733.jpg',
					 'https://www.youtube.com/watch?v=d1_JBMrrYw8',
					 'A marine on an alien planet',)

inception = media.Movie("Inception",						  
						  'http://www.kinopoisk.ru/images/film_big/447301.jpg',
						  'https://www.youtube.com/watch?v=YoHD9XEInc0',
						  'A thief is given the inverse task of planting an idea into the mind of a CEO.')

friends = media.TvShow("Friends", 
						"https://www.movieposter.com/posters/archive/main/78/MPW-39449", 
						"https://www.youtube.com/watch?v=bvEnlf9g4co",
						 "20 min")

how_i_met_your_mother = media.TvShow("How I met your mother",
									"http://vignette4.wikia.nocookie.net/how-i-met-your-mother/images/0/0a/Staffel_1.jpg/revision/latest?cb=20120207153333&path-prefix=de",
									"https://www.youtube.com/watch?v=aJtVL2_fA5w",
									"25 min")

game_of_thrones = media.TvShow("Game of Thrones",
								"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcS9McQZDr-ZA6oK7dTBJuIoclfpwVOJyX79pmUZG84ZyKh05epK",
								"https://www.youtube.com/watch?v=8ixEWrTLiZg",
								"40 min")
movies = [toy_story, avatar, inception, friends, how_i_met_your_mother, game_of_thrones]

fresh_tomatoes.open_movies_page(movies)

#print (inception.poster_image)


#print (media.Movie.VALID_RATINGS)
#print (media.Movie.__doc__)
#print (friends.duration)