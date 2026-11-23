import tkinter as tk
from tkinter import messagebox

PRICES = {
    "House Cleaning": 80,
    "Hotel Cleaning": 120,
    "Office Cleaning": 100,
    "Deep Cleaning": 150
}

def update_price(*args):
    service = service_var.get()
    price_label.config(text=f"Price: €{PRICES[service]}")

def save_booking():
    name = entry_name.get()
    phone = entry_phone.get()
    service = service_var.get()
    date = entry_date.get()
    address = entry_address.get()

    if name == "" or phone == "" or date == "":
        messagebox.showwarning("Missing!", "Please fill Name, Phone and Date!")
        return

    price = PRICES[service]
    with open("bookings.txt", "a") as f:
        f.write(f"{name} | {phone} | {service} | €{price} | {date} | {address}\n")

    messagebox.showinfo("Booked!", f"Thank you {name}!\nService: {service}\nPrice: €{price}\nRenato will call you for {date}!")
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_address.delete(0, tk.END)

def view_bookings():
    try:
        with open("bookings.txt", "r") as f:
            all_bookings = f.read()
        if all_bookings == "":
            all_bookings = "No bookings yet!"
    except:
        all_bookings = "No bookings yet!"
    messagebox.showinfo("All My Bookings", all_bookings)

app = tk.Tk()
app.title("Renato Cleaning - Booking App V2")
app.geometry("400x520")
app.configure(bg="white")

tk.Label(app, text="Renato Cleaning", font=("Arial", 20, "bold"), bg="white", fg="#2563eb").pack(pady=10)
tk.Label(app, text="Booking App V2 - With Price!", bg="white").pack()

tk.Label(app, text="Your Name:", bg="white").pack(pady=(10,0))
entry_name = tk.Entry(app, width=35)
entry_name.pack()

tk.Label(app, text="Phone:", bg="white").pack(pady=(10,0))
entry_phone = tk.Entry(app, width=35)
entry_phone.pack()

tk.Label(app, text="Service:", bg="white").pack(pady=(10,0))
service_var = tk.StringVar(value="House Cleaning")
service_var.trace("w", update_price)
tk.OptionMenu(app, service_var, "House Cleaning", "Hotel Cleaning", "Office Cleaning", "Deep Cleaning").pack()

price_label = tk.Label(app, text="Price: €80", bg="white", font=("Arial", 14, "bold"), fg="green")
price_label.pack(pady=5)

tk.Label(app, text="Date:", bg="white").pack(pady=(5,0))
entry_date = tk.Entry(app, width=35)
entry_date.pack()

tk.Label(app, text="Address in Madrid:", bg="white").pack(pady=(10,0))
entry_address = tk.Entry(app, width=35)
entry_address.pack()

tk.Button(app, text="BOOK NOW ✅", bg="#2563eb", fg="white", font=("Arial", 14, "bold"), width=20, command=save_booking).pack(pady=15)
tk.Button(app, text="VIEW ALL BOOKINGS 📋", bg="white", fg="#2563eb", font=("Arial", 11, "bold"), width=22, command=view_bookings).pack()

app.mainloop()
