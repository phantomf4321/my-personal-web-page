from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def about():
    return render_template('index.html')


app.run(debug=True)