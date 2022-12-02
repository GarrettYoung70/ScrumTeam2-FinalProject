from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *
from .db_connection_utility import *


#@app.route("/", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def user_options():
    
    form = UserOptionForm()
    if request.method == 'POST' and form.validate_on_submit():
        option = request.form['option']

        if option == "1":
            return redirect('/admin')
        else:
            return redirect("/reservations")
    
    return render_template("options.html", form=form, template="form-template")

@app.route("/admin", methods=['GET', 'POST'])
def admin():
    # Initialize validate variable
    validate = ""
    form = AdminLoginForm()
    if(request.method == 'POST'):
        if(form.validate_on_submit()):
            # Get username and password from forms
            username = request.form['username']
            password = request.form['password']
            
            # Query database to see if username/password combo exists
            if(query_db(username, password) == True):
                # If username and password match entry listed in the mysql database
                validate = "Logged success!"
            else:
                # If username and password do not match any entry listed in the mysql database
                validate = "Incorrect username or password! Please try again."
        pass
    # Pass validate variable to render_template() to be rendered on web page
    return render_template("admin.html", form=form, template="form-template", validate = validate)

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():

    form = ReservationForm()

    return render_template("reservations.html", form=form, template="form-template")