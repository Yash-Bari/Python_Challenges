from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    current_datetime = datetime.now()
    return render_template('index.html', current_datetime=current_datetime)

if __name__ == '__main__':
    app.run(debug=True)
