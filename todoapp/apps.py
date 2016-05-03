# -*- coding: utf-8 -*-
from flask import Flask, request, flash, url_for, redirect, render_template, abort, Response
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *

def create_new_todo():
    todo = Todo(request.form['title'], request.form['text'])
    db.session.add(todo)
    db.session.commit()

def edit_todo(todo_item, todo_id):
    todo_item.title = request.form['title']
    todo_item.text = request.form['text']
    todo_item.done = ('done.%d' % todo_id) in request.form
    db.session.commit()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html',
        todos = Todo.query.order_by(Todo.pub_date.desc()).all()
    )

@app.route('/new/', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        create_new_todo()
        return redirect(url_for('index'))
    return render_template('new.html')

@app.route('/todos/<int:todo_id>', methods = ['GET', 'POST'])
def show_or_update(todo_id):
    todo_item = Todo.query.get(todo_id)
    if request.method == 'GET':
        return render_template('view.html', todo = todo_item)
    edit_todo(todo_item, todo_id)
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True)
