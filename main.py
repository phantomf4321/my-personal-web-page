from flask import *
from defaults import Defaults

app = Flask(__name__)


@app.route('/')
def index():
    D1 = Defaults()
    about_data = [{"birthday": "25 May 2001", "birthdate": "2001/03/25", "age": D1.claculate_age()}]
    return render_template('index.html', data=about_data[0])

@app.route('/about')
def about():
    return redirect(url_for('index') + '#about')
app.run(debug=True)