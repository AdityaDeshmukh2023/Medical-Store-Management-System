import csv
import os
import tkinter as tk
from tkinter import ttk, simpledialog

class MedicalStore:
    def __init__(self, master):
        self.master = master
        master.title("Medical Store Management System")

        self.medicines = {}
        self.purchase_history = {}

        # Create the main frame
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(padx=20, pady=20)

        # Create the menu
        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Save and Exit", command=self.save_and_exit)

        # Create the main content area
        self.create_main_content()

    def create_main_content(self):
        # Add Medicine
        self.add_medicine_frame = tk.Frame(self.main_frame)
        self.add_medicine_frame.pack(pady=10)

        tk.Label(self.add_medicine_frame, text="Add Medicine:").pack(side=tk.LEFT)
        self.add_medicine_button = tk.Button(self.add_medicine_frame, text="Add", command=self.add_medicine)
        self.add_medicine_button.pack(side=tk.LEFT, padx=10)

        # Update Medicine
        self.update_medicine_frame = tk.Frame(self.main_frame)
        self.update_medicine_frame.pack(pady=10)

        tk.Label(self.update_medicine_frame, text="Update Medicine:").pack(side=tk.LEFT)
        self.update_medicine_button = tk.Button(self.update_medicine_frame, text="Update", command=self.update_medicine)
        self.update_medicine_button.pack(side=tk.LEFT, padx=10)

        # Delete Medicine
        self.delete_medicine_frame = tk.Frame(self.main_frame)
        self.delete_medicine_frame.pack(pady=10)

        tk.Label(self.delete_medicine_frame, text="Delete Medicine:").pack(side=tk.LEFT)
        self.delete_medicine_button = tk.Button(self.delete_medicine_frame, text="Delete", command=self.delete_medicine)
        self.delete_medicine_button.pack(side=tk.LEFT, padx=10)

        # Display Medicines
        self.display_medicines_frame = tk.Frame(self.main_frame)
        self.display_medicines_frame.pack(pady=10)

        tk.Label(self.display_medicines_frame, text="Display Medicines:").pack(side=tk.LEFT)
        self.display_medicines_button = tk.Button(self.display_medicines_frame, text="Display", command=self.display_medicines)
        self.display_medicines_button.pack(side=tk.LEFT, padx=10)

        # Record Purchase
        self.record_purchase_frame = tk.Frame(self.main_frame)
        self.record_purchase_frame.pack(pady=10)

        tk.Label(self.record_purchase_frame, text="Record Purchase:").pack(side=tk.LEFT)
        self.record_purchase_button = tk.Button(self.record_purchase_frame, text="Record", command=self.record_purchase)
        self.record_purchase_button.pack(side=tk.LEFT, padx=10)

        # Display Purchase History
        self.display_purchase_history_frame = tk.Frame(self.main_frame)
        self.display_purchase_history_frame.pack(pady=10)

        tk.Label(self.display_purchase_history_frame, text="Display Purchase History:").pack(side=tk.LEFT)
        self.display_purchase_history_button = tk.Button(self.display_purchase_history_frame, text="Display", command=self.display_purchase_history)
        self.display_purchase_history_button.pack(side=tk.LEFT, padx=10)

                # Exit Program
        self.exit_program_frame = tk.Frame(self.main_frame)
        self.exit_program_frame.pack(pady=10)

        tk.Label(self.exit_program_frame, text="Exit Program:").pack(side=tk.LEFT)
        self.exit_program_button = tk.Button(self.exit_program_frame, text="Exit", command=self.save_and_exit)
        self.exit_program_button.pack(side=tk.LEFT, padx=10)
    def add_medicine(self):
        name = simpledialog.askstring("Add Medicine", "Enter medicine name:")
        if name:
            price = self.get_positive_float("Enter price per unit:")
            quantity = self.get_positive_integer("Enter quantity available:")
            self.medicines[name] = {"price": price, "quantity": quantity}
            print("Medicine added successfully!")

    def update_medicine(self):
        name = simpledialog.askstring("Update Medicine", "Enter medicine name to update:")
        if name and name in self.medicines:
            price = self.get_positive_float("Enter new price per unit:")
            quantity = self.get_positive_integer("Enter new quantity available:")
            self.medicines[name] = {"price": price, "quantity": quantity}
            print("Medicine details updated successfully!")
        else:
            print("Medicine not found!")

    def delete_medicine(self):
        name = simpledialog.askstring("Delete Medicine", "Enter medicine name to delete:")
        if name and name in self.medicines:
            del self.medicines[name]
            print("Medicine deleted successfully!")
        else:
            print("Medicine not found!")

    def display_medicines(self):
        if not self.medicines:
            print("No medicines available.")
        else:
            print("List of available medicines:")
            for name, details in self.medicines.items():
                print(f"Name: {name}, Price: {details['price']}, Quantity: {details['quantity']}")

    def record_purchase(self):
        name = simpledialog.askstring("Record Purchase", "Enter medicine name purchased:")
        if name and name in self.medicines:
            quantity = self.get_positive_integer("Enter quantity purchased:")
            total_price = self.medicines[name]["price"] * quantity
            self.purchase_history.setdefault(name, []).append({"quantity": quantity, "total_price": total_price})
            self.medicines[name]["quantity"] -= quantity
            print("Purchase recorded successfully!")
        else:
            print("Medicine not found!")

    def display_purchase_history(self):
        if not self.purchase_history:
            print("No purchase history available.")
        else:
            print("Purchase History:")
            for name, purchases in self.purchase_history.items():
                print(f"Medicine: {name}")
                for purchase in purchases:
                    print(f"Quantity: {purchase['quantity']}, Total Price: {purchase['total_price']}")

    def get_positive_float(self, prompt):
        num = float(simpledialog.askstring("Input", prompt))
        if num <= 0:
            print("Number must be positive.")
            num = self.get_positive_float(prompt)
        return num

    def get_positive_integer(self, prompt):
        num = int(simpledialog.askstring("Input", prompt))
        if num <= 0:
            print("Number must be positive.")
            num = self.get_positive_integer(prompt)
        return num

    def save_and_exit(self):
        self.save_data_to_csv()
        print("Data saved successfully. Thank you for using the Medical Store Management System.")
        self.master.destroy()

    def save_data_to_csv(self):
        file_path = r"C:\Users\Aditya\OneDrive\Pictures\python project\medical_data.csv"
        with open(file_path, "w", newline="") as csvfile:
            fieldnames = ["Type", "Name", "Price", "Quantity"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for name, details in self.medicines.items():
                writer.writerow({"Type": "Medicine", "Name": name, "Price": details["price"], "Quantity": details["quantity"]})

            for name, purchases in self.purchase_history.items():
                for purchase in purchases:
                    writer.writerow({"Type": "Purchase", "Name": name, "Price": "", "Quantity": purchase["quantity"]})

    def load_data_from_csv(self):
        if os.path.exists("medical_data.csv"):
            with open("medical_data.csv", "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if row["Type"] == "Medicine":
                        self.medicines[row["Name"]] = {"price": float(row["Price"]), "quantity": int(row["Quantity"])}
                    elif row["Type"] == "Purchase":
                        self.purchase_history.setdefault(row["Name"], []).append({"quantity": int(row["Quantity"]), "total_price": 0})

def main():
    root = tk.Tk()
    medical_store = MedicalStore(root)
    medical_store.load_data_from_csv()
    root.mainloop()

if __name__ == "__main__":
    main()