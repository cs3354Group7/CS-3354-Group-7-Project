from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
from flask_login import login_required, current_user
from .models import Note
from .models import Inventory
from .models import Money
from decimal import Decimal
from . import db

views = Blueprint('views', __name__)

@views.route("/",methods=['GET', 'POST'])
def home():
            

    return render_template('index.html', user = current_user)

# Return Purchase Page
@views.route("/purchase")
def purchase():
    return "Purchase Page"

# Return Admin Page
@views.route("/admin",methods=['GET', 'POST'])
@login_required
def admin():
    if request.method == "POST":
        dollars = request.form.get('dollars')
        quarters = request.form.get('quarters')
        dimes = request.form.get('dimes')
        nickels = request.form.get('nickels')
        pennies = request.form.get('pennies')
        machine = request.form.get('machine')
        check_machine = Money.query.filter_by(machine = machine).first()
        
        if check_machine:
            if dollars:
                check_machine.dollars = check_machine.dollars + int(dollars)
                check_machine.total = check_machine.total + int(dollars)
            if quarters:
                check_machine.quarters = check_machine.quarters + int(quarters)
                check_machine.total = check_machine.total + Decimal(check_machine.quarters) * Decimal(.25)
            if dimes:
                check_machine.dimes = check_machine.dimes + int(dimes)
                check_machine.total = check_machine.total + Decimal(check_machine.dimes) * Decimal(.10)
            if nickels:
                check_machine.nickels = check_machine.nickels + int(nickels)
                check_machine.total = check_machine.total + Decimal(check_machine.nickels) * Decimal(.05)
            if pennies:
                check_machine.pennies = check_machine.pennies + int(pennies)
                check_machine.total = check_machine.total + Decimal(check_machine.pennies) * Decimal(.01)
            db.session.commit()
        else:
            flash('Machine does not exist.', category= 'error')
    machine = Money.query.all()
    return render_template("admin.html", user = current_user, machine = machine)

@views.route("/inventory",methods=['GET', 'POST'] )
@login_required
def inventory():
    if request.method == "POST":
        item = request.form.get('item')
        qty = request.form.get('qty')
        price = request.form.get('price')
        product = Inventory.query.filter_by(item=item).first()
        
        if product:
            if qty:
                product.qty = product.qty + int(qty)
            if price:
                product.price = product.price + int(price)
            db.session.commit()
        elif len(item) < 3:
            flash('Item name must be bigger than 4 characters', category='error')
        elif price == 0:
            flash('Price must be greater than $0', category='error')
        else:
            new_item = Inventory(item=item, qty=qty, price=price)
            db.session.add(new_item)
            db.session.commit()
            flash('Item Created!', category='success')
    items = Inventory.query.all()
    return render_template("inventory.html", user = current_user, items = items)

# Return Contact Us Page
@views.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('fristName')
        last_name = request.form.get('lastName')
        note = request.form.get('note')
        mobile = request.form.get('mobile')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, email = email, first_name = first_name, last_name = last_name, mobile = mobile,)
            db.session.add(new_note)
            db.session.commit()
            flash('Message Sent', category='success')

    return render_template("contact.html", user = current_user)
 