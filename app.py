from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def Home():
    return render_template('index.html')

@app.route('/menu')
def Menu():
    return render_template('menu.html')

@app.route('/services')
def Services():
    return render_template('services.html')

@app.route('/blog')
def Blog():
    return render_template('blog.html')

@app.route('/about')
def About():
    return render_template('about.html')

@app.route('/contact')
def Contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)