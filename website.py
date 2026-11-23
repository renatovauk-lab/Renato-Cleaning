from flask import Flask, request
import os

app = Flask(__name__)
bookings = []

HOME = """
<h1 style='color:#2563eb; text-align:center;'>Renato Cleaning</h1>
<p style='text-align:center;'>Fast, honest, and clean! - Madrid, Spain</p>
<p style='text-align:center;'><a href='/'>Home</a> | <a href='/services'>Services</a> | <a href='/book'>BOOK NOW</a> | <a href='/contact'>Contact</a> | <a href='/bookings'>View Bookings</a></p>
<hr>
<h2>Welcome!</h2>
<p>We clean houses, hotels and offices in Madrid.</p>
<p><a href='/book' style='background:#2563eb; color:white; padding:10px 20px; text-decoration:none;'>BOOK YOUR CLEANING NOW ✅</a></p>
"""

SERVICES = """
<h1>Our Services & Prices</h1>
<ul>
<li>House Cleaning - €80</li>
<li>Hotel Cleaning - €120</li>
<li>Office Cleaning - €100</li>
<li>Deep Cleaning - €150</li>
</ul>
<p><a href='/book'>Book Now</a> | <a href='/'>Home</a></p>
"""

BOOK_FORM = """
<h1>Book Your Cleaning</h1>
<form method='POST'>
Name: <br><input name='name' required><br><br>
Phone: <br><input name='phone' required><br><br>
Service: <br>
<select name='service'>
<option>House Cleaning - €80</option>
<option>Hotel Cleaning - €120</option>
<option>Office Cleaning - €100</option>
<option>Deep Cleaning - €150</option>
</select><br><br>
Date: <br><input name='date' placeholder='28 Nov 2026' required><br><br>
Address: <br><input name='address'><br><br>
<button style='background:#2563eb; color:white; padding:10px 20px;'>BOOK NOW ✅</button>
</form>
<p><a href='/'>Home</a> | <a href='/bookings'>View All Bookings</a></p>
"""

@app.route('/')
def home():
    return HOME

@app.route('/services')
def services():
    return SERVICES

@app.route('/contact')
def contact():
    return "<h1>Contact</h1><p>Renato Cleaning - Madrid, Spain</p><p><a href='/'>Home</a></p>"

@app.route('/book', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        service = request.form['service']
        date = request.form['date']
        address = request.form['address']

        # Save to bookings.txt - THIS IS THE FIX!
        booking_line = f"{name} | {phone} | {service} | {date} | {address}"
        bookings.append(booking_line)
        with open("bookings.txt", "a") as f:
            f.write(booking_line + "\n")

        return f"<h1>Thank you {name}!</h1><p>Renato will call you for {date}!</p><p>Service: {service}</p><p>Booking saved to bookings.txt!</p><p><a href='/book'>Book Another</a> | <a href='/bookings'>View All Bookings</a> | <a href='/'>Home</a></p>"
    return BOOK_FORM

@app.route('/bookings')
def view():
    # Read from bookings.txt file
    all_text = ""
    try:
        with open("bookings.txt", "r") as f:
            all_text = f.read()
    except:
        all_text = ""

    # If file is empty, try memory
    if all_text.strip() == "" and bookings:
        all_text = "\n".join(bookings)

    if all_text.strip() == "":
        return "<h1>No bookings yet!</h1><p><a href='/book'>Book Now</a></p>"

    html = "<h1>All Bookings - From bookings.txt</h1><ul>"
    for b in all_text.split("\n"):
        if b.strip() != "":
            html += f"<li>{b}</li>"
    html += "</ul><p><a href='/book'>Book Another</a> | <a href='/'>Home</a></p>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
