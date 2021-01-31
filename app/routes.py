from app import app
from flask import render_template, flash, redirect, request, url_for
from app.forms import SearchForm, RegistrationForm, CheckPrizeForm
from app.models import Participant
from app import db

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/check_prize', methods=['GET', 'POST'])
def check_prize():
    form = CheckPrizeForm()
    if form.validate_on_submit():
        participant = Participant.query.filter_by(phone=form.phone.data).first()
        if participant is None or not participant.check_lottery_code(form.lottery_code.data):
            flash('Invalid phone number or lottery code')
            return redirect(url_for('check_prize'))
        else:
            return render_template('index.html', prize='Good luck next time!')
    return render_template('check_prize.html', title='Check prizes', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        participant = Participant(first_name=form.first_name.data, 
                                  last_name=form.last_name.data,
                                  phone=form.phone.data)
        code = participant.set_lottery_code(form.phone.data)
        db.session.add(participant)
        db.session.commit()
        flash('Registration complete, your lottery code is \n {}'.format(code))
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        participant = Participant.query.filter_by(phone=form.phone.data).first()
        if participant is not None: #or not user.check_password(form.password.data):
            return render_template('index.html', results=participant)  # or what you want
        else:
            flash('Phone number is not recognized!')
            return redirect(url_for('search'))
    return render_template('search.html', form=form)