from flask_wtf.file import FileAllowed, FileRequired, FileField
from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField
from wtforms.validators import DataRequired
from wtforms import SpringField


class UploadForm(FlaskForm):
      description = TextAreaField('Description', validators=[DataRequired()])
      photo = FileField('Upload Image', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Only jpg, png and jpeg is accepted')])

