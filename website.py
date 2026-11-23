from flask import Flask

app = Flask(__name__)

# PAGE 1 - HOME
@app.route("/")
def home():
    return """
    <h1>Renato Cleaning Services</h1>
    <a href="/">Home</a> | <a href="/about">About</a> | <a href="/services">Services</a> | <a href="/contact">Contact</a>
    <p>Welcome! We clean hotels and houses in Madrid.</p>
    <p>Fast, honest, and clean!</p>
    """

# PAGE 2 - ABOUT
@app.route("/about")
def about():
    return """
    <h1>About Us</h1>
    <a href="/">Home</a> | <a href="/about">About</a> | <a href="/services">Services</a> | <a href="/contact">Contact</a>
    <p>My name is Renato. I am from Philippines. I live in Madrid.</p>
    <p>I am hardworking, honest, and punctual.</p>
    """

# PAGE 3 - SERVICES
@app.route("/services")
def services():
    return """
    <h1>Our Services</h1>
    <a href="/">Home</a> | <a href="/about">About</a> | <a href="/services">Services</a> | <a href="/contact">Contact</a>
    <p>1. Hotel Housekeeping</p>
    <p>2. House Cleaning</p>
    <p>3. Deep Cleaning</p>
    <p>Price: Call us for price!</p>
    """

# PAGE 4 - CONTACT
@app.route("/contact")
def contact():
    return """
    <h1>Contact Us</h1>
    <a href="/">Home</a> | <a href="/about">About</a> | <a href="/services">Services</a> | <a href="/contact">Contact</a>
    <p>Email: porsunarenato@gmail.com</p>
    <p>Phone: 611 273 883</p>
    <p>Madrid, Spain</p>
    """

app.run(debug=False, port=5001)
