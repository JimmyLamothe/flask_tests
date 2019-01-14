#!/usr/bin/env python
import uuid
from flask import Flask, render_template, redirect, url_for, session #session = TODO
from flask_wtf import FlaskForm
from wtforms.validators import Required
from wtforms.fields import RadioField, SubmitField
from question_walker import random_tree, Tracker

app = Flask(__name__)
app.config['SECRET_KEY'] = uuid.uuid4().hex
tracker = Tracker()
tree = random_tree()

class MultipleChoice(FlaskForm):
    #to modify choices: form_name.answer.choices = [(label1, content1), (label2, content2)]
    answer = RadioField('Your answer', choices = [], validators =[Required()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    print('Index')
    global tree
    name_list = [node.name for node in tree.node_list]
    tracker.current_node = tree.root
    session['tracker'] = {}
    session['tracker']['current_index'] = tree.get_node_index(tracker.current_node)
    print(session['tracker']['current_index'])
    print(str([node.name for node in tree.node_list]))
    session.modified = True
    tracker.name_list = name_list
    return render_template('index.html')

@app.route('/question_walker/', methods = ['GET', 'POST'])
def question_walker():
    print('question_walker')
    global tree
    node = tree.node_list[session['tracker']['current_index']]
    #node = tracker.current_node
    print('Current index: ' + str(session['tracker']['current_index']))
    test_node = tree.node_list[session['tracker']['current_index']]
    print(test_node == node)
    print('Session Node: ' + test_node.name)
    print('Tracker Node: ' + node.name)
    name = node.name
    print('Current Node: ' + name)
    children = node.children
    print('Current Children: ' + str([child.name for child in children]))
    parent = node.parent
    print('Current parent: ' + parent.name)
    new_text = 'Choose a child to follow'
    if children:
        choice_list = []
        for index, child in enumerate(children):
            choice_list.append((str(index),child.name))
        print(choice_list)
        #form = YesNoQuestionForm()
        form = MultipleChoice()
        form.answer.choices = choice_list
        if form.validate_on_submit():
            print(form.answer.__dict__)
            answer = form.answer.data
            next_index = int(answer)
            next_node = children[next_index] #temp - see if dict contents have real answer
            tracker.current_node = next_node
            session['tracker']['current_index'] = tree.get_node_index(next_node)
            test_node = tree.node_list[session['tracker']['current_index']]
            session.modified = True
            return redirect(url_for('question_walker', text = new_text))
        else:
            return render_template('question_walker.html', text = new_text, form = form)
    else:
        print('End of tree')
        tree = random_tree()
        root = tree.root
        tracker.current_node = root
        session['tracker']['current_index'] = tree.get_node_index(root)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
