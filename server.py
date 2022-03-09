# the next two lines always need to be atop this server.py file 
# from collections import UserList # this is a line that's relevant for other stuff; keep out for this assignment, as it's needlessly confusing me
from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app
from user import User_cls
# import random # can refrain from this import, it's not being used on this assignment. 
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'dsadfdafdfgaf' # this key can always be some junk, it doesn't matter, as long as this line is there. 
# app = Flask(__name__)

@app.route('/')
def index():
    allUsers = User_cls.get_all()
    return render_template("index.html", display_allUsers = allUsers)

@app.route('/addNewUser')
def addNew():
    # allUsers = User_cls.get_all()
    return render_template("addNewUser.html") #, display_allUsers = allUsers)

# relevant code snippet from server.py
# from friend import Friend
@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "clr_firstName": request.form["frm_firstName"],
        "clr_lastName" : request.form["frm_lastName"],
        "clr_email" : request.form["frm_email"]
        }
    # We pass the data dictionary into the save method from the Friend class.
    User_cls.save(data)
    # Don't forget to redirect after saving to the database.
    # return redirect('/')
    # immed above replaced by immed below; need an inbetween step here, to stop dupe submissions on refresh
    return redirect('/displayIndexAgain') # this entire two-step redirect is  needed when you've got a results page. 
    

@app.route('/displayIndexAgain')
def displayIndexAgain():
    return redirect("/")

"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'

# below is flask boiler plate; exclude it and stuff won't work    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

