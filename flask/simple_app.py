from flask import Flask
from flask import render_template


'''
__name__ will name this with whatever the name space is
a simple way of saying always refer to yourself.
'''
app = Flask(__name__)


'''
view function will show on page.  route is decorator.
'''
@app.route('/')
@app.route('/<name>')# tells flask to capture whats after the forward slash as name
def index(name='Todd'):
    return render_template('index.html', name=name)


'''
four routes so we can take both floats and ints.  
they will still go to the same view
'''
@app.route('/add/<int:num1>/<int:num2>')
@app.route('/add/<float:num1>/<float:num2>')
@app.route('/add/<int:num1>/<float:num2>')
@app.route('/add/<float:num1>/<int:num2>')
def add(num1, num2):
    context = {'num1':num1, 'num2':num2}
    return render_template('add.html', **context)
    
    # could also do
    # return render_template('add.html', num1=num1, num2=num2)
    

'''
debug will keep relaoding the page on save
'''
app.run(debug=True, port=8080, host='0.0.0.0')


