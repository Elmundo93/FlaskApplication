from flask import Flask, render_template, request, redirect, url_for
from storage_json import StorageJson

app = Flask(__name__)
blog = StorageJson(data.json)

@app.route('/')
def index():
    return render_template('index.html', posts=blog.list_data())

@app.route('/create', methods=('GET','POST'))
def create():
    if request.method == 'POST':
        blog.add_data(request.form['author'], request.form['title'], request.form['content'])
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/edit/<int:id>', methods=('GET','POST'))
def edit(id):
    post = next(p for p in blog.list_data() if p['id'] == id)
    if request.method == 'POST':
        blog.update_data(id, request.form['author'], request.form['title'], request.form['content'])
        return redirect(url_for('index'))
    return render_template('edit.html', post=post)

@app.route('/delete/<int:id>', methods=('POST',))
def delete(id):
    blog.delete_data(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5000, debug=True)
