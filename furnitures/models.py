from . import db

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    products = db.relationship('Product', backref='Category', cascade="all, delete-orphan")

    def __repr__(self):
        str = "ID: {}, Name: {}, Description: {}, Image: {}\n"
        str = str.format(self.id, self.name, self.description, self.image)
        return str

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('product_id',db.Integer,db.ForeignKey('products.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'product_id') )

class Product(db.Model):
    __tablename__='products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64),nullable=False)
    short_description = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.String(128), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __repr__(self):
        str = "Id: {}, Name: {}, Short Description: {}, Description: {}, Image: {}, Price: {}, Size: {}\n" 
        str =str.format( self.id, self.name, self.short_description, self.description,self.image, self.price, self.size, self.category_id)
        return str

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    date_purchased = db.Column(db.DateTime)
    date_shipped = db.Column(db.DateTime)
    status = db.Column(db.Boolean, default=False)
    delivery_cost = db.Column(db.Float)
    subtotal_cost = db.Column(db.Float)
    total_cost = db.Column(db.Float)
    firstname = db.Column(db.String(64))
    lastname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    products = db.relationship("Product", secondary=orderdetails, backref="orders")

    def __repr__(self):
        str = "Id: {}, Date Purchased: {}, Date Shipped: {}, Status: {}, Delivery Cost: {}, Sub Total Cost: {}, Total Cost: {}, First name:{}, Last name:{}, Email: {}, Phone:{}\n" 
        str =str.format( self.id, self.date_purchased, self.date_shipped, self.status, self.delivery_cost, self.subtotal_cost, self.total_cost, self.firstname, self.lastname, self.email, self.phone)
        return str

