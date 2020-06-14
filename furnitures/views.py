from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import Category, Product, Order
from datetime import datetime
from .forms import CheckoutForm
from . import db

bp = Blueprint('main', __name__)

@bp.route('/') 
def index():
    categories = Category.query.order_by(Category.name).all()
    return render_template('home.html', categories = categories)

@bp.route('/category/<int:categoryid>/')
def category(categoryid):
    categories = Category.query.order_by(Category.name).all()
    products = Product.query.filter(Product.category_id == categoryid)
    return render_template('products.html', categories = categories, products = products)

@bp.route('/products')
def search():
    search = request.args.get('search').lower()
    searchPara = '%{}%'.format(search) 
    products = Product.query.filter(Product.short_description.like(searchPara)).all() 
    categories = Category.query.order_by(Category.name).all()
    return render_template('products.html', categories = categories, products = products)

@bp.route('/product/<int:productid>/')
def product(productid):
    product = Product.query.get(productid)
    categories = Category.query.order_by(Category.name).all()
    return render_template('product-detail.html', categories = categories, product = product)

@bp.route('/cart/', methods=['POST','GET'])
def cart():
    categories = Category.query.order_by(Category.name).all()
    if 'order_id'in session.keys():
        order = Order.query.get(session['order_id'])
    else:
        order = None

    if order is None:
        order = Order(date_purchased=datetime.now(), date_shipped=datetime.now(), status = False, delivery_cost = 49, total_cost=0)
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except:
            print('failed at creating a new order')
            order = None
    
    if order is not None:
        updateOrderPrice(order)
    
    product_id = request.values.get('product_id')
    if product_id is not None and order is not None:
        product = Product.query.get(product_id)
        if product not in order.products:
            try:
                order.products.append(product)
                db.session.commit()
            except:
                return 'There was an issue adding the item to your basket'
            return redirect(url_for('main.cart'))
        else:
            flash('Item already in basket')
            return redirect(url_for('main.product', productid=product.id))
    return render_template('cart.html', categories = categories, order = order )

@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        del session['order_id']
    return redirect(url_for('main.cart'))

@bp.route('/deleteorderitem/', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        product_to_delete = Product.query.get(id)
        try:
            order.products.remove(product_to_delete)
            db.session.commit()
            return redirect(url_for('main.cart'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.cart'))


@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    categories = Category.query.order_by(Category.name).all()
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        updateOrderPrice(order)
       
        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.lastname = form.lastname.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.delivery_address = form.delivery_address.data
            order.billing_address = form.billing_address.data
            total_price = 0
            for product in order.products:
                total_price = total_price + product.price
            order.subtotal_cost = total_price
            order.total_cost = total_price + order.delivery_cost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                return redirect(url_for('main.ordersuccess'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', categories = categories, form = form, order=order)

@bp.route('/ordersuccess/')
def ordersuccess():
    categories = Category.query.order_by(Category.name).all()
    return render_template('order-success.html', categories = categories)

def updateOrderPrice(order):
    db.session.add(order)
    totalprice = 0
    for p in order.products:
        totalprice = totalprice + p.price
    order.subtotal_cost =totalprice
    order.total_cost = order.subtotal_cost + order.delivery_cost
    try:
        db.session.commit()
    except: 
        return 'There was an issue updating the order'
    return order