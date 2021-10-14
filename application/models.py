from .database import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    username = db.Column(db.String, unique = True)
    email = db.Column(db.String, unique = True)

class Article(db.Model):
    __tablename__ = 'article'
    article_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    title = db.Column(db.String)
    content = db.Column(db.String)
    authors = db.relationship("User", secondary = 'article_authors')    

class ArticleAuthors(db.Model):
    __tablename__ = 'article_authors'
    article_id = db.Column(db.Integer, db.ForeignKey("article.article_id"), primary_key = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"), primary_key = True, nullable = False)
