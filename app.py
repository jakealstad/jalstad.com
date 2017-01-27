from flask import Flask, render_template
from flaskext.markdown import Markdown
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)
Markdown(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
