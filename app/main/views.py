from . import main
from flask import render_template,redirect,url_for,request,flash
from flask_login import login_required,current_user
from .forms import UpdateProfile,BlogForm,CommentForm
from ..models import User,Blog,Comment
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

@main.route('/comment/<int:id>', methods=["GET", "POST"])
@login_required
def comment(id):
    comments = Comment.query.filter_by(blog_id = id)
    blog = Blog.query.filter_by(id=id).first()
    form = CommentForm()
    description = form.description.data
    if form.validate_on_submit():
          
            comment = Comment(description = description , user = current_user , blog = blog)

            db.session.add(comment)
            db.session.commit()

            return redirect(url_for('main.comment', id = id))

            

   
    title = 'comments'
    return render_template("comments.html" , blog=blog , comments = comments ,form = form)

