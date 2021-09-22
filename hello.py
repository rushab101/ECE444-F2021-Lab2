from flask import Flask
from flask import Flask, render_template, session, redirect,url_for,flash
from flask_bootstrap import Bootstrap
from datetime import datetime
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
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
        if old_name and old_name != form.name.data:
            flash("Looks like you've changed your name!")
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template("index.html", form=form, name=session.get('name'))
    '''
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)
    '''
    #return render_template("index.html",current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template("user.html", name=name,  current_time=datetime.utcnow())

if __name__ == "__main__":
    app.run(debug=True)