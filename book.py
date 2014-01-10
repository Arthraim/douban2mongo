# encoding: utf-8
from mongoengine import *

class Book (Document):
    title = StringField()
    pub = StringField()
    link = StringField(unique=True)
    rating = StringField()
    date = StringField()
    tags = ListField()
    comment = StringField()