from flask import Flask, render_template, url_for, redirect,request


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/square',methods = ['GET','POST'])
def square():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('square.html')


@app.route('/rectangle',methods = ['GET','POST'])
def rectangle():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('rectangle.html')

@app.route('/triangle',methods = ['GET','POST'])
def triangle():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('triangle.html')
