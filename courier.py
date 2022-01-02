from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Package, Courier, Package_Locker
from . import db

import secrets

courier = Blueprint('courier', __name__)

def gen_id():
	return secrets.token_hex(15)

@courier.route('/courier/create', methods=['GET'])
@login_required
def create():
	return render_template('courier_create.html')

@courier.route('/courier/create', methods=['POST'])
@login_required
def create_post():
	name = request.form['name']

	new_package = Courier(name=name, courier_id=gen_id())

	db.session.add(new_package)
	db.session.commit()

	return redirect(url_for('main.index'))
