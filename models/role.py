from app.extensions import db


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.relationship('User', back_populates='role')
    isAdmin = db.Column(db.Boolean, default=False)
    desc = db.Column(db.String(100))

    def __repr__(self):
        return 'Role %r' % self.id
