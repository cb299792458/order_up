from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Table
from app import db

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    tables = db.session.query(Table).all()
    return render_template('orders.html', tables=tables)