from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField
from wtforms.validators import DataRequired


class ManufacturerForm(FlaskForm):
    name = StringField('Manufacturer name',
                       validators=[DataRequired()])
    description = TextAreaField('Description')
    country = StringField('Country', validators=[DataRequired()])
    certificates = TextAreaField('Certificates')
    internal_id = StringField('Internal ID',
                              validators=[DataRequired()])
    submit = SubmitField('Add manufacturer')
