# encoding: utf-8
from mongoengine import *

class Movie (Document):
    title = StringField()
    link = StringField(unique=True)
    rating = StringField()
    date = StringField()
    tags = ListField()
    comment = StringField()