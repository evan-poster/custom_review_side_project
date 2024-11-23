#this file helps make sure the user dont leave ne\o fields empty and 
#automatically creates textboxs abd buttons for the html and allow user to upload pictures 

from flask_wtf import FlaskForm  #Makes it easier for error messages, validate data and protects forums from security risk
from wtforms.validators import DataRequired,FileField #check if the form field have been filled it cant be empty 
from wtforms import StringField, TextAreaField,FileField,SubmitField ,IntegerField
from flask_wtf.file import FileRequired, FileAllowed # makes sure the user uploads a picture and make sure which file types to use 


#depending on justin i might not need this 
# automatically create Text boxes and buttons in the html 
class """the name of the html class here"""(FlaskForm):

    userId = StringField("UserId", validators=[DataRequired()])
    comment = TextAreaField("Comment", validators=[DataRequired()])
    upload = FileField("Upload Picture", validators=[FileRequired(),FileAllowed(['jpg','png','jpeg'])])
    rating = IntegerField("Rating", validators=[DataRequired()])
    submit = SubmitField("Post Review")
   