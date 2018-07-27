from flask import Flask, render_template, url_for
import re
import uuid


from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config = True
   
class UserDetails(object):
    """user to handle activities related to a user"""
    def__init__(self):
       # a list to hold all user objects
       self.user_list = []
    
    def register(self, username, email, password, cnfpassword):
        user_details = {}

        for user in self.user_list:
            if username == user['username'] or  user['email'] == email:

               return "username and email already exists"

        else:
             if not re.match("^[a-zA-Z0-9_]*$", username):
             or not re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$", email):
                return "username  or email can only contain alphanumeric characters"

             elif len(username.strip()) < 3:
                return "username must be more than three characters"

             elif password !=cnfpassword:
                return "passwords do not match"

            elif len(password) < 6:
                return "password too short"   

            else:
                #regiser user if all the details are valid
                user_details['username'] = username
                user_details['email'] = email
                user_details['password'] = password
                userdetails['id'] = uuid.uuid1()
                self.user_list.append(user_details)
                return "registration succesfull"
    def login(self, username, password):

        for user in self.user_list:
            if username == user['username'] and password == user['password']:
                return "succesfull"  
            else:
            return "Incorrect password or username"   

    def reset_password(self, email, new_password):
        for user in self.user_list:
            if email == user['email']:
                user['password'] = new_password
            else:
                return "Incorrect email"                        

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def about():
    form = LoginForm()

#     if form.validate_on_submit():
#         return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

#     return render_template('login.html',form=form)


# @app.route('/registration', methods=['GET', 'POST'])
# def register():
#     form = Registrationform(request.form)
#     if request.method == 'POST' and form.validate():
#         user = user(form.username.data, form.email.data, form.password.data, form.confirmpassword.data)
#         flash('Thanks forregistering')
#         return redirect(url_for('login'))
#         return render_templete('register.html', form=form)

# @app.route('/Database')
# def index():
#     return render_template("Database.html")

# @app.route('/base')
# def index():
#     return render_template("base.html")


if __name__== '__main__':
    app.run()