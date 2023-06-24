from flask import Flask, render_template

app = Flask(__name__)

@app.route('/name')
def name():
    return render_template('name.html', name = 'Neelam Deka', email = 'neelamdeka20@gmail.com')

@app.route('/')
def index():
    return render_template('index.html', link = "<a href=url_for('/name')></a>")

if __name__ == '__main__':
    app.run(debug=True)