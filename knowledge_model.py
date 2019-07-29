from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

	pass 
	__tablename__ = 'articles'
	num_article = Column(Integer, primary_key=True)
	topic= Column(String)
	link = Column(String)
	rating= Column(Integer)


	def __repr__(self):
		return ("if you want to read about {}\n"
				" here is the link: {}\n"
				"I gave it a rating of: {}\n").format(self.topic,self.link,self.rating,)

# friends = Knowledge(num_article= 1 ,topic- "3 things you didn't know anout the show friends",rating = 8)