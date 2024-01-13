from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def ask_story():
    return render_templates("storylist.html", stories=stories.values())

@app.route('/questions')
def ask_question():
    story_select = request.args["story_select"]
    story = stories[story_select]
    
    prompts = story.prompts 
    
    return render_template("questions.html", story_select= story_select, title = story.title, prompts = prompts)

@app.route('/story')
def show_story():
     story_select = request.args["story_select"]
     story = stories[story_select]
     
     text = story.gernerate(request.args)
     
     return render_template('story.html', title=story.title,text=text)