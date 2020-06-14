from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email, Length

# form used in cart
class CheckoutForm(FlaskForm):
    firstname = StringField("First name", validators=[InputRequired()])
    lastname = StringField("Last name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), email()])
    phone = StringField("Phone number", validators=[InputRequired(), Length(min=10, max=16)])
    delivery_address = StringField("Delivery address", validators=[InputRequired()])
    billing_address = StringField("Billing address", validators=[InputRequired()])
    submit = SubmitField("Complete Order")
 