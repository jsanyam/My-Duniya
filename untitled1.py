import logging
from flask import Flask, render_template
import sys

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def hello_world():
    return render_template('base.html')


if __name__ == '__main__':
    app.run()