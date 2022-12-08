from flask import current_app as app
from flask import redirect, render_template, url_for, request, flash

from .forms import *
from .db_connection_utility import *
from .cost_matrix import *


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
    # Initialize variables
    totalCost = None
    validate = ""
    chart = None
    form = AdminLoginForm()
    if(request.method == 'POST'):
        if(form.validate_on_submit()):
            # Get username and password from forms
            username = request.form['username']
            password = request.form['password']
            
            # Query database to see if username/password combo exists
            if(query_db(username, password) == True):
                # If username and password match entry listed in the mysql database
                validate = "Printing Seating Chart..."
                chart = getSeatingChart()
                totalCost = getTotalCost()
            else:
                # If username and password do not match any entry listed in the mysql database
                validate = "Incorrect username or password! Please try again."
                chart = None
                totalCost = None
        pass
    # Pass validate variable and seating chart to render_template() to be rendered on web page
    return render_template("admin.html", form=form, template="form-template", validate=validate, chart=chart, totalCost=totalCost)

@app.route("/reservations", methods=['GET', 'POST'])
def reservations():
    error = ""
    form = ReservationForm()
    chart = getSeatingChart()
    if(request.method == 'POST'):
        if(form.validate_on_submit()):
            first_name = request.form['first_name']
            #last_name = request.form['last_name']
            row = int(request.form['row']) - 1 
            seat = int(request.form['seat']) - 1
            
            # If seat is already taken, print error message instead of writing to file
            if(chart[row][seat] == "X"):
                error = "Error! The requested seat has already been reserved! Please try again."
            
            # If seat is available, update file and chart
            else:
                #Yang Put code for Print Reservation here
                resCode = 'testResCode'
            

                with open('reservations.txt', 'a') as f:
                    f.write(first_name + ', ' + str(row) + ', ' + str(seat) + ', ' + resCode + '\n')
                    f.close()
                chart = getSeatingChart()
    return render_template("reservations.html", form=form, template="form-template", chart=chart, error=error)

