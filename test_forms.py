#!/usr/bin/env python

from flask import Flask, render_template, redirect, url_for
from flask_wtf import Form
from wtforms.fields import RadioField, SubmitField
from question_walker import random_tree, Tracker

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
questions = ['Is it compiled?', 'Does it run on a VM?']
guesses = ['Python', 'Java', 'C++']
root = random_tree()
tracker = Tracker()
tracker.current_node = root

class YesNoQuestionForm(Form):
    answer = RadioField('Your answer', choices=[('yes', 'Yes'), ('no', 'No')])
    submit = SubmitField('Submit')

choice_list = [('yes', 'Yes'), ('no', 'No')]

class MultipleChoiceForm(YesNoQuestionForm):
    def __init__(self, choice_list):
        self.answer = RadioField('Your answer', choices = choice_list)

with app.app_context():
    test_YN = YesNoQuestionForm()
    test_MC = MultipleChoiceForm()
    print(test_YN.__dict__)
    print(test_MC.__dict__)
