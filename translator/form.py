from flask_wtf import FlaskForm
from wtforms import TextAreaField, SelectField, validators, SubmitField


class TranslateForm(FlaskForm):
    source_language = SelectField('Source Language', choices=[
        ('auto', 'Detect Language'),
        ('en', 'English'),
        ('yo', 'Yoruba'),
        ('ig', 'Igbo'),
        ('ha', 'Hausa')])
    
    target_language = SelectField('Target Language', choices=[
        ('en', 'English'), 
        ('yo', 'Yoruba'),
        ('ig', 'Igbo'),
        ('ha', 'Hausa')])

    text = TextAreaField('Text to Translate', validators=[
        validators.input_required()])
    submit = SubmitField("Translate")