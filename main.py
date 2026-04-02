import tkinter as tk
from tkinter import ttk, messagebox

class RestaurantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant App")

        self.menu = {
            "Fries": 2,
            "Lunch": 3,
            "Burger": 3.5,
            "Pizza": 4,
            "Cheese Burger": 2.5,
            "Drinks": 1
        }

        self.rates = {"USD": 1, "KES": 130}

        frame = ttk.Frame(root, padding=20)
        frame.pack()

        ttk.Label(frame, text="Restaurant Menu", font=("Arial", 18, "bold")).grid(row=0, columnspan=2, pady=10)

        self.entries = {}

        # MENU ITEMS
        for i, (item, price) in enumerate(self.menu.items(), 1):
            ttk.Label(frame, text=f"{item} ($ {price})").grid(row=i, column=0, padx=10, pady=5)
            entry = ttk.Entry(frame, width=5)
            entry.grid(row=i, column=1)
            self.entries[item] = entry

        # CURRENCY (outside loop!)
        self.currency = tk.StringVar(value="USD")
        ttk.Label(frame, text="Currency").grid(row=i+1, column=0)

        ttk.Combobox(
            frame,
            textvariable=self.currency,
            values=["USD", "KES"],
            state="readonly"
        ).grid(row=i+1, column=1)

        ttk.Button(frame, text="Place Order", command=self.calculate).grid(row=i+2, columnspan=2, pady=10)

    def calculate(self):
        total = 0
        currency = self.currency.get()   # FIXED
        rate = self.rates[currency]
        symbol = "KSh" if currency == "KES" else "$"

        summary = "Order Summary:\n\n"

        for item, entry in self.entries.items():
            qty = entry.get()

            if qty.isdigit() and int(qty) > 0:
                qty = int(qty)
                price = self.menu[item] * rate
                cost = qty * price
                total += cost

                summary += f"{item}: {qty} x {symbol}{price} = {symbol}{cost}\n"

        if total > 0:
            summary += f"\nTotal: {symbol}{total}"
            messagebox.showinfo("Order", summary)   # FIXED
        else:
            messagebox.showerror("Error", "Please select at least one item.")

# RUN APP
root = tk.Tk()   # FIXED
root.geometry("340x450")
RestaurantApp(root)
root.mainloop()