from . import auth
from flask import render_template


@auth.route('/login',methods=['GET','POST'])
def login():
    return render_template('login.html')


@auth.route('/register',methods = ["GET","POST"])
def register():
    return render_template('register.html')


@auth.route('/logout')
def logout():
    pass