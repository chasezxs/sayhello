#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    :author: zhouxiaosong
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, ValidationError


class HelloForm(FlaskForm):
    def validate_body(self, field):
        if not isinstance(field, str) and field.data != '宝塔镇河妖':
            raise ValidationError('The captcha value must be "宝塔镇河妖".')

    name = StringField('Name', validators=[DataRequired(message=u'abc'), Length(1, 20)])
    message = TextAreaField('message', validators=[DataRequired(), Length(1, 200)])
    body = StringField('天王盖地虎', validators=[DataRequired()])
    submit = SubmitField('提交')
