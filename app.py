from flask import Flask
from flask import render_template
import os

app = Flask(__name__, template_folder='html')

# Return Home Page
@app.route("/")
def home():
    return render_template('index.html')

# Return Purchase Page
@app.route("/purchase")
def purchase():
    return "Purchase Page"

# Return Admin Page
@app.route("/admin")
def admin():
    return "Admin Page"

# Return login Page
@app.route("/login")
def login():
    return "Login Page"

# Return Sign Up Page
@app.route("/sign-up")
def signUp():
    return "Sign Up Page"

# Return Contact Us Page
@app.route("/contact")
def contact():
    return "Contact Page"

if __name__ == "__main__":
    app.run(debug=True)