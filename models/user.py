from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    login = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.relationship('Role', back_populates='user')
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'), nullable=False)
    personal_number = db.Column(db.String(20), nullable=False)
    residency = db.Column(db.String(50))
    phone = db.Column(db.String(15))

    def __repr__(self):
        return 'User %r' % self.id

    def to_string(self):
        if self.role.isAdmin:
            print("Yes, I'm admin")
        else:
            print("No, I'm not admin")
        print("My role is " + self.role.desc())