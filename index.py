import blockdiag

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/diagram/<diag>', methods=['GET', 'POST'])
def diagram(diag):
    '''See blockdiag/utils/bootstrap.py for an example of using the
    library programatically which is very poorly documented. We need
    to parse, build, then draw and ideally return an svg string.
    '''
    return diag

if __name__ == '__main__':
    app.run()
