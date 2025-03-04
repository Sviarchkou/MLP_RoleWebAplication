from extensions import db


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False)
    desc = db.Column(db.String(200))
    user = db.relationship('User', back_populates='role')

    def __repr__(self):
        return 'Role %r' % self.id
