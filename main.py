# TASK 1
# Importing the necessary classes and methods
from flask import Flask,jsonify,request,render_template,make_response,send_file,redirect
import requests
# Creating an instance of Flask class
app = Flask(__name__)

# Displaying a Hello World string
# The decorator (@app.route('/')) followed by the method to invoke
@app.route('/')
def index():
    return 'Hello World - Priyadarshini J R'

# Displaying the list of authors with the count of posts
@app.route('/authors')
def authors():
    # Initialising a dictionary
    detail = dict()
    # Fetching data from the given URLs in the json format
    author_data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    post_data = requests.get('https://jsonplaceholder.typicode.com/posts').json()

    # For every author, initially setting count to 0
    for author in author_data:
        detail[author['name']] = 0
        userid = author['id']

        # Comparing the id of an author with the userId of every post
        for post in post_data:
            if userid == post['userId']:
                detail[author['name']] += 1
    # Dictionary cannot be returned as such, use jsonify
    return jsonify(detail)

# To set cookies containing age and name
@app.route('/setcookie')
def setcookie():
    # Response to be displayed
    resp = make_response('Cookies set with name and age.')
    resp.set_cookie('Name','Priyadarshini')
    resp.set_cookie('Age','21')
    return resp

# Viewing the cookies set
@app.route('/getcookies')
def getcookie():
    ck = request.cookies
    # Dictionary of cookies (name value pair) must be jsonified
    return jsonify(ck)

# Denying requests to a page
@app.route('/robots.txt')
def deny():
    return 'You should not be here.'

# Rendering an HTML document
@app.route('/html')
def render_html():
    # profile.html must be placed within the templates folder
    # to be used by render_template
    return render_template('profile.html')

# Rendering an image
@app.route('/image')
def render_image():
    return send_file('sunset.jpg', mimetype='image/gif')

# Displaying a textbox, sending the data as POST to another endpoint
# Log the data to stdout
# This endpoint accepts both GET and POST requests
@app.route('/input',methods = ["GET","POST"])
def input_func():
    # If the method is POST, getting the data from the form
    # Redirect to a different endpoint while passing the data
    if request.method == "POST":
        name = request.form['input']
        return redirect('/output/' + name)

    # Displaying the form
    return render_template('input.html')

# The data entered is passed in the URL
@app.route('/output/<name>')
def output(name):
    # Output it to stdout
    print("You entered : " + name)
    return 'Welcome. Check your stdout for the name entered.'

# Run the file
if __name__ == '__main__':
    app.run()