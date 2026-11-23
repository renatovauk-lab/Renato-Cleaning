from flask import Flask, request
app = Flask(__name__)
bookings = []

@app.route('/')
def home():
    return """<h1 style='color:#2563eb; text-align:center;'>Renato Cleaning</h1>
    <p style='text-align:center;'>Fast, honest, and clean! - Madrid</p>
    <p style='text-align:center;'><a href='/book'>BOOK NOW ✅</a> | <a href='/services'>Services</a> | <a href='/contact'>Contact</a></p>
    <h2>Welcome!</h2><p>We clean houses, hotels and offices in Madrid.</p>"""

@app.route('/services')
def services():
    return """<h1>Services & Prices</h1><ul>
    <li>House Cleaning - €80</li>
    <li>Hotel Cleaning - €120</li>
    <li>Office Cleaning - €100</li>
    <li>Deep Cleaning - €150</li></ul>
    <p><a href='/book'>Book Now</a> | <a href='/'>Home</a></p>"""

@app.route('/contact')
def contact():
    return "<h1>Contact</h1><p>Renato Cleaning - Madrid, Spain</p><p><a href='/'>Home</a></p>"

@app.route('/book', methods=['GET','POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        service = request.form['service']
        date = request.form['date']
        bookings.append(f"{name} | {service} | {date}")
        return f"<h1>Thank you {name}!</h1><p>Renato will call you for {date}!</p><p>Service: {service}</p><p><a href='/book'>Book Another</a> | <a href='/'>Home</a></p>"
    return """<h1>Book Your Cleaning</h1>
    <form method='POST'>
    Name:<br><input name='name' required><br><br>
    Phone:<br><input name='phone' required><br><br>
    Service:<br><select name='service'>
    <option>House Cleaning - €80</option>
    <option>Hotel Cleaning - €120</option>
    <option>Office Cleaning - €100</option>
    <option>Deep Cleaning - €150</option></select><br><br>
    Date:<br><input name='date' placeholder='28 Nov 2026' required><br><br>
    Address:<br><input name='address'><br><br>
    <button style='background:#2563eb; color:white; padding:10px 20px;'>BOOK NOW ✅</button>
    </form><p><a href='/'>Home</a></p>"""

@app.route('/bookings')
def view():
    if not bookings:
        return "<h1>No bookings yet!</h1><p><a href='/book'>Book Now</a></p>"
    html = "<h1>All Bookings</h1><ul>"
    for b in bookings:
        html += f"<li>{b}</li>"
    html += "</ul><p><a href='/'>Home</a></p>"
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
