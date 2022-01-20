from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def login_required(e):
  return render_template('500.html'), 500

def create_app():
	app = Flask(__name__)

	app.config['SECRET_KEY'] = 'secret-key-goes-here'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

	db.init_app(app)

	login_manager = LoginManager()
	login_manager.login_view = 'auth'
	login_manager.init_app(app)

	@app.before_first_request
	def create_tables():
		db.create_all()

	from .models import User

	@login_manager.user_loader
	def load_user(user_id):
		# since the user_id is just the primary key of our user table, use it in the query for the user
		return User.query.get(int(user_id))

	# blueprint for auth routes in our app
	from .auth import auth as auth_blueprint
	app.register_blueprint(auth_blueprint)

	# blueprint for non-auth parts of app
	from .main import main as main_blueprint
	app.register_blueprint(main_blueprint)

	from .package import package as package_blueprint
	app.register_blueprint(package_blueprint)

	from .courier import courier as courier_blueprint
	app.register_blueprint(courier_blueprint)

	from .package_locker import package_locker as package_locker_blueprint
	app.register_blueprint(package_locker_blueprint)

	from .car import car as car_blueprint
	app.register_blueprint(car_blueprint)

	app.register_error_handler(500, login_required)

	return app