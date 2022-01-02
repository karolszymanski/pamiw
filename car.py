from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required
from .models import Car
from . import db

import secrets

car = Blueprint('car', __name__)

def gen_id():
	return secrets.token_hex(15)

@car.route('/car/create', methods=['GET'])
@login_required
def create():
	return render_template('car_create.html')

@car.route('/car/create', methods=['POST'])
@login_required
def create_post():
	model = request.form['model']

	new_car = Car(model=model, car_id=gen_id())

	db.session.add(new_car)
	db.session.commit()

	return redirect(url_for('main.index'))
