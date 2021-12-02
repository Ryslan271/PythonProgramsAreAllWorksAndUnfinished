from models import db_session
from models.news import News
from datetime import date

db_session.global_init('sqlite.db')

post = News()
post.login = 'login'
post.password_page = '123'
post.date = date.fromisoformat('2020-01-01')

session = db_session.create_session()
session.add(post)
session.commit()
