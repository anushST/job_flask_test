from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import (FileField, SelectMultipleField, SubmitField,
                     StringField, TextAreaField)
from wtforms.validators import DataRequired

from app.settings import ALLOWED_IMAGE_EXTENSIONS


class BrandForm(FlaskForm):
    logo = FileField('Logo', validators=[
        FileRequired(),
        FileAllowed(ALLOWED_IMAGE_EXTENSIONS, 'Only images!')
    ])
    name = StringField('Brand name', validators=[DataRequired()])
    description = TextAreaField('Description')
    internal_id = StringField('Internal ID',
                              validators=[DataRequired()])
    manufacturer_ids = SelectMultipleField('Manufacturers', coerce=int,
                                           validators=[DataRequired()])
    submit = SubmitField('Add brand')
