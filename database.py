from dotenv import load_dotenv
load_dotenv()

# create user order_up with password '9uCxydbt';
# create database order_up_dev with owner order_up;

# Regardless of the lint error you receive,
# load_dotenv must run before running this
# so that the environment variables are
# properly loaded.
from app import app, db
from app.models import Employee, Menu, MenuItem, MenuItemType, Table, Order, OrderDetail


with app.app_context():
    db.drop_all()
    db.create_all()

    employee1 = Employee(name="Margot", employee_number=1234, password="password")
    db.session.add(employee1)

    employee2 = Employee(name="Robbie", employee_number=4321, password="password")
    db.session.add(employee2)

    beverages = MenuItemType(name="Beverages")
    db.session.add(beverages)
    entrees = MenuItemType(name="Entrees")
    db.session.add(entrees)
    sides = MenuItemType(name="Sides")
    db.session.add(sides)

    dinner = Menu(name="Dinner")
    db.session.add(dinner)
    lunch = Menu(name='Lunch')
    db.session.add(lunch)

    fries = MenuItem(name="French Fries", price=3.50, type=sides, menu=dinner)
    db.session.add(fries)
    drp = MenuItem(name="Dr. Pepper", price=1.0, type=beverages, menu=dinner)
    db.session.add(drp)
    jambalaya = MenuItem(name="Jambalaya", price=21.98, type=entrees, menu=dinner)
    db.session.add(jambalaya)

    salad = MenuItem(name="Salad", price=5.25, type=sides, menu=lunch)
    db.session.add(salad)
    sandwich = MenuItem(name="Sandwich", price=9.99, type=entrees, menu=lunch)
    db.session.add(sandwich)
    milk = MenuItem(name="Milk", price=1.0, type=beverages, menu=lunch)
    db.session.add(milk)

    tables=[ Table(number=i,capacity=4) for i in range(1,10) ]
    for table in tables:
        db.session.add(table)

    order1 = Order(finished=False, employee=employee1, table=tables[0])
    db.session.add(order1)
    detail1 = OrderDetail(order=order1, menu_item=jambalaya)
    db.session.add(detail1)

    order2 = Order(finished=False, employee=employee2, table=tables[1])
    db.session.add(order2)
    detail2 = OrderDetail(order=order1, menu_item=fries)
    db.session.add(detail2)
    detail3 = OrderDetail(order=order1, menu_item=drp)
    db.session.add(detail3)


    db.session.commit()