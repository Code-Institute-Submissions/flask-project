from flask import Blueprint, render_template
from flask import current_app as app


# Set up a Blueprint
admin_bp = Blueprint('admin_bp', __name__,
                     template_folder='templates',
                     static_folder='static')