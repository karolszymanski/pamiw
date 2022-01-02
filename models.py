from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
	__tablename__ = 'Users'
	id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(1000))

class Package(db.Model):
	__tablename__ = 'Packages'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100))
	details = db.Column(db.String(1000))
	status = db.Column(db.String(100))
	package_id = db.Column(db.String(100), unique=True)
	courier = db.Column(db.String(100), db.ForeignKey('Couriers.courier_id'))
	package_locker = db.Column(db.String(100), db.ForeignKey('Package_Lockers.package_locker_id'))

class Courier(db.Model):
	__tablename__ = 'Couriers'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	courier_id = db.Column(db.String(100), unique=True)
	package = db.Column(db.String(100), db.ForeignKey('Packages.package_id'))
	car = db.Column(db.String(100), db.ForeignKey('Cars.car_id'))

class Car(db.Model):
	__tablename__ = 'Cars'
	id = db.Column(db.Integer, primary_key=True)
	car_id = db.Column(db.String(100), unique=True)
	courier = db.Column(db.String(100), db.ForeignKey('Couriers.courier_id'))
	model = db.Column(db.String(100))

class Package_Locker(db.Model):
	__tablename__ = 'Package_Lockers'
	id = db.Column(db.Integer, primary_key=True)
	package_locker_id = db.Column(db.String(100), unique=True)
	name = db.Column(db.String(100))
