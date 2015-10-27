import webbrowser
class Video():
	def __init__(self, title, poster_image, trailer):
		self.title = title
		self.poster_image = poster_image
		self.trailer = trailer

	def show_trailer(self):
		webbrowser.open(self.trailer)


class Movie(Video):
	"""This class provides a way to store movie related information"""

	VALID_RATINGS = ['G','PG', 'PG-13', 'R']

	def __init__(self, title, 
		poster_image, trailer, storyline):
		Video.__init__(self, title, poster_image, trailer)
		self.storyline = storyline
		

class TvShow(Video):
	def __init__(self, title, poster_image, trailer, duration):
		Video.__init__(self, title, poster_image, trailer)
		self.duration = duration