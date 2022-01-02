from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Package, Courier, Package_Locker
from . import db

import secrets

package_locker = Blueprint('package_locker', __name__)

def gen_id():
	return secrets.token_hex(15)

@package_locker.route('/package_locker/create', methods=['GET'])
@login_required
def create():
	return render_template('package_locker_create.html')

@package_locker.route('/package_locker/create', methods=['POST'])
@login_required
def create_post():
	name = request.form['name']

	new_package_locker = Package_Locker(name=name, package_locker_id=gen_id())

	db.session.add(new_package_locker)
	db.session.commit()

	return redirect(url_for('main.index'))
