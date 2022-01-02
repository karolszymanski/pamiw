from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Package, Courier, Package_Locker
from . import db

import secrets

main = Blueprint('main', __name__)

def gen_package_id():
	return secrets.token_hex(15)

@main.route('/')
@login_required
def index():
	packages = Package.query.all()

	return render_template('main_index.html', packages=packages)
