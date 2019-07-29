from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(topic, link, rating):
	article_object = Knowledge(  
        topic=topic,
        link=link,
        rating=rating)
	session.add(article_object)
	session.commit()
#add_article("3 things you didn't know about the show friends", "http://mentalfloss.com/article/56565/25-things-you-might-not-know-about-friends",8)


def query_all_articles():
	articles = session.query(
    Knowledge).all()
	return articles

query_all_articles()
# print(query_all_articles())

def query_article_by_topic(their_topic):
	articles = session.query(
       	Knowledge).filter_by(		
		topic=their_topic).first()
	return articles
print(query_article_by_topic("3 things you didn't know about the show friends"))


def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass


