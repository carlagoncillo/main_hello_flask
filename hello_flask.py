from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'YAY FLASK!!'  # Return the string 'Hello World!' as a response

# /success route returns string "Success!" on our website
@app.route('/success')
def success():
    return "Success!"

# use angeled brackets to add variables to your routes
@app.route('/student/<name>')
def one_students(name):
    return f"Hello, {name}"

# you can have more than one variable in your routes
@app.route('/student/<name>/<other_name>')
def two_students(name, other_name):
    return f"Hello, {name} and {other_name}"

# make sure to import 'render_template' at the top of your file
@app.route('/hello_world')
def hello():
    return render_template('hello_world.html')

@app.route('/hello_world/<name_from_python>/<int:num>')
def hello_name(name_from_python, num):
    student_info = [
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]
    return render_template('hello_with_name.html', name_to_html = name_from_python, num = num, students = student_info)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
