from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
username = 'Bob'
friends = ['Alice', 'Carl', 'Dina', 'Eric']


@app.route('/')
def index():
    return render_template("index.html")


@app.get('/user')
def user_get():
    content = render_template("user.html", name=username, friends=friends)
    print(content)
    return content


@app.post('/user')
def user_post():
    friend = request.form['friend_name']
    friends.append(friend)
    return redirect(url_for('user_get'))


if __name__ == '__main__':
    app.run()
