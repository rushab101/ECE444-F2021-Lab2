from flask import Flask
from flask import Flask, render_template, session, redirect,url_for,flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required,Email
from wtforms.fields.html5 import EmailField


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    email = EmailField("What is your UofT Email address?", validators=[Required(), Email()])
    submit = SubmitField('Submit')




app = Flask(__name__)
bootstrap = Bootstrap(app)
#curr_time = datetime.now()
moment = Moment(app)
app.config['SECRET_KEY'] = 'key'

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name and old_name != form.name.data:
            flash("Looks like you've changed your name!")
        if old_email and old_email != form.email.data:
            flash("Looks like you've changed your email!")
        session['name'] = form.name.data
        session['email'] = form.email.data
        session['is_uofT'] = isValidEmail(form.email.data)
        return redirect(url_for('index'))
    return render_template("index.html", form=form, name=session.get('name'),email=session.get('email'),is_uofT = session.get('is_uofT'))
    '''
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
    '''
    #return render_template("index.html",current_time=datetime.utcnow())

def isValidEmail(email):
    b = email.split('@')
    return b[-1].find('utoronto') != -1



@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name,  current_time=datetime.utcnow())

if __name__ == "__main__":
    app.run(debug=True)