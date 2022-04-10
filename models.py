from settings import db
from sqlalchemy import Column, Integer, Text
from datetime import datetime


class User(db.Model):

    student_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    dob = db.Column(db.String(60))
    amount_due = db.Column(db.String(300))


    def __str__(self):
        return self.first_name + self.last_name + str(self.dob)

