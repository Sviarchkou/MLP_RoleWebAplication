from tkinter.constants import CASCADE
from extensions import db

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    desc = db.Column(db.Text, nullable=False)
    user = db.relationship('User', back_populates='message')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete=CASCADE), nullable=False)

    def __repr__(self):
        return 'Message %r' % self.id

