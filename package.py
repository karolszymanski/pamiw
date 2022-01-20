from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Package, Courier, Package_Locker
from . import db

import secrets

package = Blueprint('package', __name__)


def gen_id():
	return secrets.token_hex(15)

@package.route('/package/create', methods=['GET'])
@login_required
def create():
	couriers = Courier.query.all()
	package_lockers = Package_Locker.query.all()
	return render_template('package_create.html', couriers=couriers, package_lockers=package_lockers)

@package.route('/package/create', methods=['POST'])
@login_required
def create_post():
	title = request.form['title']
	details = request.form['details']
	courier = request.form['courier']
	package_locker = request.form['package_locker']

	new_package = Package(title=title, details=details, status='accepted', package_id=gen_id(), courier=courier, package_locker=package_locker)

	db.session.add(new_package)
	db.session.commit()

	return redirect(url_for('main.index'))

@package.route('/package/edit/<int:id>')
@login_required
def edit(id):
	couriers = Courier.query.all()
	package = Package.query.filter_by(id=id).first()
	return render_template('package_edit.html', package=package, couriers=couriers)

@package.route('/package/edit/<int:id>', methods=['POST'])
@login_required
def edit_post(id):
	package = Package.query.filter_by(id=id).first()

	title = request.form['title']
	details = request.form['details']
	courier = request.form['courier']
	status = request.form['status']

	if title:
		package.title = title

	if details:
		package.details = details

	if courier:
		package.courier = courier

	if status:
		package.status = status

	db.session.commit()

	return redirect(url_for('main.index'))

@package.route('/package/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
	package = Package.query.filter_by(id=id).first()
	db.session.delete(package)
	db.session.commit()
	return redirect(url_for('main.index'))

@package.route('/package/details/<int:id>')
@login_required
def details(id):
	package = Package.query.filter_by(id=id).first()
	courier = Courier.query.filter_by(courier_id=package.courier).first()
	locker = Package_Locker.query.filter_by(package_locker_id=package.package_locker).first()
	return render_template('package_details.html', package=package, courier=courier, locker=locker)
