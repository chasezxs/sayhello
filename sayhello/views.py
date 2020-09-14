#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    :author: zhouxiaosong
"""
from flask import redirect, url_for, flash, render_template, request
from wtforms import ValidationError

from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        message = form.message.data
        body = form.body.data
        form.validate_body(body)
        message = Message(name=name, body=message)
        db.session.add(message)
        db.session.commit()
        flash('Your message hava been sent to the world!')
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    per_page = app.config['PER_PAGE']
    pagination = Message.query.order_by(Message.timestamp.desc()).paginate(page, per_page)
    messages = pagination.items
    return render_template('index.html', form=form, messages=messages, pagination=pagination)
