# app/models.py
from peewee import Model, SqliteDatabase, CharField

db = SqliteDatabase('contacts.db')

class Contact(Model):
    first_name = CharField()
    last_name = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Contact])
