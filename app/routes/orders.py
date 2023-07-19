from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Table, Employee
from app.forms import TableAssignmentForm
from app import db

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    tables = db.session.query(Table).all()
    employees = db.session.query(Employee).all()
    form = TableAssignmentForm()
    form.tables.choices=[(t.id,t.id) for t in tables]
    form.servers.choices=[(e.id,e.name) for e in employees]
    return render_template('orders.html', tables=tables, form=form)