from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import Table, Employee, Order
from app.forms import TableAssignmentForm
from app import db

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/",methods=['GET','POST'])
@login_required
def index():
    form = TableAssignmentForm()

    tables = db.session.query(Table).all()
    employees = db.session.query(Employee).all()
    open_orders = Order.query.filter(Order.finished == False)
        
    busy_tables = [order.table_id for order in open_orders]
    open_tables = [table for table in tables if table.id not in busy_tables]

    form.table.choices=[(t.id,t.id) for t in open_tables]
    form.employee.choices=[(e.id,e.name) for e in employees]

    your_id = int(current_user.get_id())
    your_tables = [table for table in tables if table.orders and table.orders[0].employee.id==your_id]

    if form.validate_on_submit():
        table=form.table.data
        employee=form.employee.data
        order = Order(finished=False,employee_id=employee,table_id=table)
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('.index'))

    return render_template('orders.html', tables=tables, form=form, your_tables=your_tables)

@bp.route("/close_table/<int:id>",methods=['POST'])
@login_required
def close(id):
    order = Table.query.get(id).orders[0]
    for detail in order.details:
        db.session.delete(detail)

    db.session.delete(order)
    db.session.commit()

    return redirect(url_for('.index'))
