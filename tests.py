from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('pza_selector.html', title='My Projects')

if __name__ == '__main__':
    app.run(debug=True)