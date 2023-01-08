from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """user will input their customized info"""
    return render_template("input.html")

@app.route('/story')
def tell_stories():
    input_place = request.args.get('input_place')
    input_noun = request.args.get('input_noun')
    input_verb = request.args.get('input_verb')
    input_adjective = request.args.get('input_adjective')
    input_plural_noun = request.args.get('input_plural_noun')
    return render_template('storytime.html', place = input_place, noun = input_noun, 
    verb = input_verb, adjective = input_adjective, plural_noun = input_plural_noun)