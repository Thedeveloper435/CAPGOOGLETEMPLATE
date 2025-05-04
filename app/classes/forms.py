# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired, NumberRange
from wtforms.validators import URL, Email, DataRequired
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField, URLField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    image = FileField("Image") 
    submit = SubmitField('Post')
    role = SelectField('Role', choices=[('Player', 'Player'), ('Captain', 'Team Captain'), ('Coach', 'Coach')])
    league_category = SelectField('League Category',choices=[("Recreational","Recreational"),("Competition","Competition"),("College", "College")], validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
     

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    submit = SubmitField('Blog')

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

class ClinicForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    streetAddress = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zipcode = StringField('Zipcode',validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
    location = StringField('Location')
    availability = StringField('Availability', validators=[DataRequired()])
    quality = StringField('Quality', validators=[DataRequired()])
    capacity = IntegerField('Capacity', validators=[DataRequired()])
    schedule = TextAreaField('Weekly schedule', validators=[DataRequired()])
    image = FileField('Image')


from wtforms import SelectField

class ReviewForm(FlaskForm):
   name = SelectField('Field Name', choices=[
    ("Cesar Chavez Field", "Cesar Chavez Field"),
    ("Alameda Point Soccer Field", "Alameda Point Soccer Field"),
    ("SFF Soccer - Mission Bay Field", "SFF Soccer - Mission Bay Field"),
    ("Hampton Field", "Hampton Field"),
    ("Tom Bates Regional Sports Complex", "Tom Bates Regional Sports Complex"),
    ("Chabot College Soccer Field", "Chabot College Soccer Field"),
    ("William Payne Field", "William Payne Field"),
    ("Livermore Community Park", "Livermore Community Park"),
    ("Laney College Soccer Field", "Laney College Soccer Field"),
    ("Crocker Amazon Soccer Field", "Crocker Amazon Soccer Field"),
    ("Burrell Field", "Burrell Field"),
    ("Richard H. Sheridan Soccer Field", "Richard H. Sheridan Soccer Field"),
    ("Alden E. Oliver Sports Park", "Alden E. Oliver Sports Park"),
    ("San Pablo Park", "San Pablo Park"),
    ("Maxwell Family Field", "Maxwell Family Field"),
    ("Mather Sports Center North Soccer Field", "Mather Sports Center North Soccer Field"),
    ("Street Soccer USA","Street Soccer USA"),
    ("South Sunset Soccer Fields", "South Sunset Soccer Fields"),
    ("Beach Chalet Athletic Fields", "Beach Chalet Athletic Fields"),
    ("Soccer Field", "Soccer Field"),
    ("Elmhurst Soccer Field","Elmhurst Soccer Field"),
    ("Oakland Soccer Club", "Oakland Soccer Club")
    ("Golden Gate Park Soccer Field","Golden Gate Park Soccer Field"),
    ("Franklin Field", "Franklin Field"), 
    ("UC Berkeley Recreational Sports", "UC Berkely Recreational Sports") 
])


   subject = SelectField('Experience Category', choices=[
        ("Field Condition", "Field Condition"),
        ("Booking Experience", "Booking Experience"),
        ("Facilities", "Facilities"),
        ("Staff", "Staff"),
        ("Pricing", "Pricing"),
        ("Other", "Other")
    ]) 
    
   rating = SelectField('Rating', choices=[
        ('1', '1 - Poor'),
        ('2', '2 - Fair'),
        ('3', '3 - Good'),
        ('4', '4 - Very Good'),
        ('5', '5 - Excellent')
    ])
   text = TextAreaField('Your Review', validators=[DataRequired()])
   submit = SubmitField('Post Review')

class ReplyForm(FlaskForm):
    text = TextAreaField('Reply', validators=[DataRequired()])
    submit = SubmitField('Post')

