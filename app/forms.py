from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import ValidationError, DataRequired, regexp
from app.models import Participant
import phonenumbers

class CheckPrizeForm(FlaskForm):
    phone = StringField('Phone number', validators=[DataRequired()])
    lottery_code =  StringField('Lottery code', validators=[DataRequired()])
    submit = SubmitField('Submit')

class SearchForm(FlaskForm):
    phone = StringField('Phone number', validators=[DataRequired()])
    search = SubmitField('Search',
                       render_kw={'class': 'btn btn-success btn-block'})

class RegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    phone = StringField('Phone number')
    image = FileField('Image File')
    submit = SubmitField('Register')
    
    def validate_phone(self, phone):
        participant = Participant.query.filter_by(phone=phone.data).first()
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')
    
    def validate_image(self, image):
        pass