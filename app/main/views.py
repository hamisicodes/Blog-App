from . import main
from flask import render_template,redirect,url_for,request,flash
from flask_login import login_required,current_user
from .forms import UpdateProfile,BlogForm
from ..models import User,Blog
from .. import db

@main.route('/')
def index():
    blogs = Blog.query.all()
    title = 'welcome'
    return render_template('index.html', title=title ,blogs=blogs)

@main.route('/blogs' ,methods=["GET", "POST"])
@login_required
def blogs():
    form  = BlogForm()
    title = form.title.data
    blog = form.blog.data
    blogs = Blog.query.all()

    if form.validate_on_submit():
        new_blog = Blog(title = title ,description = blog , user = current_user)

        db.session.add(new_blog)
        db.session.commit()

        blogs = Blog.query.all()

        return redirect(url_for('main.blogs'))


    title = 'all blogs'
    return render_template("blogs.html" ,blogs = blogs , form = form)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('update.html',form =form)

