from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        password = request.form.get('password')
        return render_template('index.html', name=name, age=age, email=email)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
