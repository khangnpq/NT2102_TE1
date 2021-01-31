from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Participant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(36))
    last_name = db.Column(db.String(84))
    phone = db.Column(db.String(20))
    lottery_code = db.Column(db.String(128))

    def __repr__(self):
        return '<Participant {}>'.format(self.first_name)
    
    def set_lottery_code(self, phone):
        lottery_code = generate_password_hash(phone)
        self.lottery_code = generate_password_hash(lottery_code)
        return lottery_code
    
    def check_lottery_code(self, lottery_code):
        return check_password_hash(self.lottery_code, lottery_code)