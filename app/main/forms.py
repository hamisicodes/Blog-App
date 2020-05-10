from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField
from wtforms.validators import Required,Email,EqualTo


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')