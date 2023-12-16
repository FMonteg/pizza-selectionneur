from flask import Flask, render_template
import json
import os

app = Flask(__name__)

project_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(project_dir)

@app.route('/')
def index():
    with open('data/pza_compositions.json', 'r') as json_file:
        pizzas = json.load(json_file)
    return render_template('pza_selector.html', title='Sélecteur de pizza', pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)