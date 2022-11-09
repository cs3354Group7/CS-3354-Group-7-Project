from flask import Flask

app = Flask(__name__)

# Return Home Page
@app.route("/")
def home():
    return "Home Page"

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