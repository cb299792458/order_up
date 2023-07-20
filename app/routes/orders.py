from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import Table, Employee, Order, MenuItem, OrderDetail
from app.forms import TableAssignmentForm, OrderForm
from app import db
from collections import defaultdict

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/",methods=['GET','POST'])
@login_required
def index():
    form = TableAssignmentForm()
    order_form = OrderForm()

    tables = db.session.query(Table).all()
    employees = db.session.query(Employee).all()
    open_orders = Order.query.filter(Order.finished == False)
    menu_items = MenuItem.query.all()
        
    busy_tables = [order.table_id for order in open_orders]
    open_tables = [table for table in tables if table.id not in busy_tables]

    form.table.choices=[(t.id,t.id) for t in open_tables]
    form.employee.choices=[(e.id,e.name) for e in employees]

    your_id = int(current_user.get_id())
    your_tables = [table for table in tables if table.orders and table.orders[0].employee.id==your_id]

    
    order_form.table.choices=[(t.id,t.id) for t in your_tables]
    order_form.item.choices=[(i.id,i.name) for i in menu_items]

    sums=defaultdict(int)
    for table in your_tables:
        for item in table.orders[0].details:
            sums[table.id]+=item.menu_item.price

    if form.validate_on_submit():
        table=form.table.data
        employee=form.employee.data
        order = Order(finished=False,employee_id=employee,table_id=table)
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('.index'))
    
    if order_form.validate_on_submit():
        item=order_form.item.data
        table=order_form.table.data
        order_id=Table.query.get(table).orders[0].id

        order_detail=OrderDetail(menu_item_id=item, order_id=order_id)
        db.session.add(order_detail)
        db.session.commit()
        return redirect(url_for('.index'))

    return render_template('orders.html',
                           tables=tables,
                           form=form, 
                           your_tables=your_tables, 
                           sums=sums, 
                           order_form=order_form)

@bp.route("/close_table/<int:id>",methods=['POST'])
@login_required
def close(id):
    order = Table.query.get(id).orders[0]
    for detail in order.details:
        db.session.delete(detail)

    db.session.delete(order)
    db.session.commit()

    return redirect(url_for('.index'))


