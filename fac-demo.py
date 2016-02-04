from flask import Flask, render_template, request
import random

app = Flask(__name__)

regionlist = ['Asian', 'Slavic', 'Romance']
def pick_region(word):
    print random.choice(regionlist)
    return random.choice(regionlist)

@app.route('/', methods=['GET', 'POST'])
def intro():
    if request.method == 'GET':
        return render_template('ea-frontpage.html')
    elif request.method == 'POST':
        return render_template('ea-frontpage.html', word = request.form["word"], results = pick_region(request.form["word"]))

if __name__ == '__main__':
    app.run(debug=True)

