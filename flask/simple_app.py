from flask import Flask

'''
__name__ will name this with whatever the name space is
a simple way of saying always refer to yourself.
'''
app = Flask(__name__) 

@app.route('/')
def index():
    return 'Hello World'

app.run(debug=True, port=8080, host='0.0.0.0')


