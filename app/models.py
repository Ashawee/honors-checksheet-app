from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    honors_id = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
        
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def verify_honorsID(self, given_id):
        return self.honors_id == given_id
        
    def __repr__(self):
        return '<User: {}>'.format(self.username)
        
        
#user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    
    __tablename__ = 'roles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    users = db.relationship('User', backref='role', lazy='dynamic')
    
    def __repr__(self):
        return '<Role: {}>'.format(self.name)
    
class Checksheet(db.Model):
    
    __tablename__ = 'checksheets'
    
    id = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(60), index=True)
    firstName = db.Column(db.String(60), index=True)
    honors_id = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(60), unique=True, index=True)
    admitted = db.Column(db.String(60))
    dupontCode = db.Column(db.Integer)
    status = db.Column(db.String(60))
    comments = db.Column(db.String(60))
    term = db.Column(db.String(60))
    coCur1 = db.Column(db.String(200))
    coCurDate1 = db.Column(db.Date())
    coCur2 = db.Column(db.String(200))
    coCurDate2 = db.Column(db.Date())
    coCur3 = db.Column(db.String(200))
    coCurDate3 = db.Column(db.Date())
    coCur4 = db.Column(db.String(200))
    coCurDate4 = db.Column(db.Date())
    coCur5 = db.Column(db.String(200))
    coCurDate5 = db.Column(db.Date())
    coCur6 = db.Column(db.String(200))
    coCurDate6 = db.Column(db.Date())
    coCur7 = db.Column(db.String(200))
    coCurDate7 = db.Column(db.Date())
    coCur8 = db.Column(db.String(200))
    coCurDate8 = db.Column(db.Date())
    fsemHN = db.Column(db.String(60))
    fsemHNDate = db.Column(db.String(60))
    hnCourse1 = db.Column(db.String(60))
    hnCourse1Date = db.Column(db.String(60))
    hnCourse2 = db.Column(db.String(60))
    hnCourse2Date = db.Column(db.String(60))
    hnCourse3 = db.Column(db.String(60))
    hnCourse3Date = db.Column(db.String(60))
    hnCourse4 = db.Column(db.String(60))
    hnCourse4Date = db.Column(db.String(60))
    hnCourse5 = db.Column(db.String(60))
    hnCourse5Date = db.Column(db.String(60))
    researchCourse = db.Column(db.String(60))
    researchCourse = db.Column(db.String(60))
    capstoneCourse = db.Column(db.String(60))
    capstoneCourse = db.Column(db.String(60))
    hon201 = db.Column(db.String(60))
    hon201 = db.Column(db.String(60))
    leadership = db.Column(db.String(60))
    mentoring = db.Column(db.String(60))
    portfolio1 = db.Column(db.String(60))
    portfolio2 = db.Column(db.String(60))
    portfolio3 = db.Column(db.String(60))
    portfolio4 = db.Column(db.String(60))
    exit = db.Column(db.String(60))
    
    def __repr__(self):
        return '<Checksheet: {}>'.format(self.name)
    
    
    
    