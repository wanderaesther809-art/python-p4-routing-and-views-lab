from flask import Flask, request, make_response

app = Flask(__name__)

# 1. Index View
@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# 2. Print String View
@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return parameter

# 3. Count View (Corrected for the test)
@app.route('/count/<int:parameter>')
def count(parameter):
    result = ""
    for i in range(parameter):
        result += f"{i}\n"
    return result

# 4. Math View
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = 0
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    
    return str(result) # Must be a string for Flask

if __name__ == '__main__':
    app.run(port=5555, debug=True)