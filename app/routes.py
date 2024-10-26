# app/routes.py
from flask import Blueprint, render_template

# Create a blueprint named 'bp'
bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/destinations')
def destinations():
    return render_template('destinations.html')

@bp.route('/culture')
def culture():
    return render_template('culture.html')

@bp.route('/tips')
def tips():
    return render_template('tips.html')

@bp.route('/contact')
def contact():
    return render_template('contact.html')
