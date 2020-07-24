#!/usr/bin/env python3

from flask import Flask, request, render_template, \
                  redirect

from model_sqlite import *

app = Flask(__name__)
initTable()

@app.route('/')
def index():
    return render_template('index.html', last_added = getAllCodes())

@app.route('/create')
def create():
    uid = createCode()
    return redirect("{}edit/{}".format(request.host_url, uid))
    
@app.route('/edit/<string:uid>/')
def edit(uid):
    row = getCode(uid)

    if row is None:
        return render_template('error.html', uid = uid)

    d = dict(
        uid=uid,
        code=row[1],
        lang=row[2],
        url="{}view/{}". format(request.host_url, uid))

    return render_template('edit.html', **d)

@app.route('/publish', methods=['POST'])
def publish():
    code = request.form['code']
    uid = request.form['uid']
    lang = request.form['lang']

    updateCode(uid, code, lang)

    return redirect("{}{}/{}".format(request.host_url,
                                     request.form['submit'],
                                     uid))

@app.route('/view/<string:uid>/')
def view(uid):
    row = getCode(uid)
    if row is None:
        return render_template('error.html',uid=uid)
    d = dict(
        uid=uid,
        code=row[1],
        lang=row[2],
        url="{}view/{}".format(request.host_url, uid))

    return render_template('view.html', **d)

@app.route('/admin/')
def admin():
    pass

if __name__ == '__main__':
    app.run()

