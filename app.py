# import Services.BookStatistics as bs
# import constants as cs
# import Views.MainMenuView as mmv

# def main():
#     # books = fm.read_books(cs.book_file_name)
#     bs.calculate_each_genre(cs.book_file_name)
#     print("Printinu is pagrindinio")
#     mmv.print_main_menu()
# main()

# Pakeistas = 15

# print(Pakeistas)


# import importuojamas as imp

# kopija = imp.importuojamas_kintamasis

# imp.importuota_funkcija(kopija)

# objektas = imp.importuojama_klase()
# print(__name__)
# from importuojamas import importuota_funkcija as ifun
# from importuojamas import importuojama_klase as iklas

# ifun(15)
# import Classes.Book as bk # Importuojamas visas failas 

# bk.Book()

# from Classes.Book import Book # Importuojamas elementas

# Book()

# from Classes import Book,Reader # Importuojami keli failai


# # Define the table data
# data = [
#     {"Name": "Alice", "Age": 25, "City": "New York"},
#     {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
#     {"Name": "Charlie", "Age": 35, "City": "Chicago"},
# ]

# # Create the table header
# header = f"{'Name':<10} {'Age':<5} {'City':<15}"
# separator = "-" * len(header)

# # Print the header
# print(header)
# print(separator)

# # Print each row of data
# for row in data:
#     print(f"{row['Name']:<10}| {row['Age']:<5}| {row['City']:<15}")

# import tkinter as tk
# from tkinter import ttk

# def calculate_sum():
#     try:
#         num1 = float(entry_num1.get())
#         num2 = float(entry_num2.get())
#         result.set(f"The sum is: {num1 + num2}")
#     except ValueError:
#         result.set("Please enter valid numbers!")

# # Create the main window
# root = tk.Tk()
# root.title("Simple Calculator")

# # Number 1 input
# label_num1 = ttk.Label(root, text="Enter first number:")
# label_num1.grid(column=0, row=0, padx=10, pady=5, sticky=tk.W)
# entry_num1 = ttk.Entry(root)
# entry_num1.grid(column=1, row=0, padx=10, pady=5)

# # Number 2 input
# label_num2 = ttk.Label(root, text="Enter second number:")
# label_num2.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
# entry_num2 = ttk.Entry(root)
# entry_num2.grid(column=1, row=1, padx=10, pady=5)

# # Button to calculate sum
# button_calculate = ttk.Button(root, text="Calculate Sum", command=calculate_sum)
# button_calculate.grid(column=0, row=2, columnspan=2, pady=10)

# # Result display
# result = tk.StringVar()
# result_label = ttk.Label(root, textvariable=result, foreground="blue")
# result_label.grid(column=0, row=3, columnspan=2, pady=5)

# # Run the application
# root.mainloop()
