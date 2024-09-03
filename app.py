from flask import Flask, request, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
    return '''
        <h1>Simple Calculator</h1>
        <form method="POST" action="/calculate">
            <input type="number" name="num1" placeholder="Number 1" required>
            <select name="operation">
                <option value="add">+</option>
                <option value="subtract">-</option>
            </select>
            <input type="number" name="num2" placeholder="Number 2" required>
            <input type="submit" value="Calculate">
        </form>
    '''


@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2

    return f'<h1>Result: {result}</h1><a href="/">Go back</a>'


if __name__ == '__main__':
    app.run(debug=True)
