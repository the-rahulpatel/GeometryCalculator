from flask import Flask, render_template, url_for, redirect,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/square')
def square_main():
    return render_template('square.html')

@app.route('/square',methods = ['GET','POST'])
def square():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Post':
            x = request.form.get('xname')
            y = request.form.get('yname')
            return render_template('square.html',x=x,y=y)
    elif request.method == 'GET':
        return redirect(url_for('index'))
@app.route('/rectangle',methods = ['GET','POST'])


def rectangle():
    if request.method == 'POST':
        x = request.form.get('xname')
        y = request.form.get('yname')
        return f"The x is {x} and y is {y}"
    return render_template('rectangle.html')


@app.route('/triangle',methods = ['GET','POST'])
def triangle():
    if request.method == 'POST':
        x = request.form.get('xname')
        y = request.form.get('yname')
        z = request.form.get('zname')
        return f"The x is {x} and y is {y} and the z is {z}"
    return render_template('triangle.html')





