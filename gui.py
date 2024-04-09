import tkinter as tk
from tkinter.ttk import OptionMenu
import dataProcessing
from tkinter import ttk
import sv_ttk


def search_stock():
    query = symbol_entry.get()
    processed_data = dataProcessing.fetch_closing_prices(query)
    
    # Clear any existing result label
    result_label.config(text="")

    # Display the processed data or an error message
    if processed_data is not None:
        result_label.config(text=processed_data)
    else:
        result_label.config(text="No data found for the entered stock symbol.")


   
def add_stock_entry():
    global stock_entries
    
    # Create the new frame for the stock entry
    new_row = len(stock_entries) + 3
    
    
    # Create the dropdown menu
    symbol_label = tk.Label(config_frame, text="Enter stock symbol:", anchor=tk.W)
    symbol_label.grid(row=new_row, column=0, padx=5, pady=5)

    symbol_entry = tk.Entry(config_frame)
    symbol_entry.grid(row=new_row, column=1, padx=5, pady=5)

    # Adjust row position of "Added stock entry" label
    add_button.grid(row=new_row, column=0, padx=5, pady=5)

    # Update the stock_entries list
    stock_entries.append((symbol_entry, config_frame))


# Everything below are edits to the GUI

root = tk.Tk()
root.geometry("600x400")
root.title("Portfolio Optimization")



# Create a frame for welcome message
welcome_frame = tk.Frame(root)
welcome_frame.grid(row=0, columnspan=2, padx=5, pady=10)

# Create a label for welcome message
welcome_label = tk.Label(welcome_frame, text="Welcome to my Portfolio Optimization for my Invesco Internship Project!", font=('Arial', 16))
welcome_label.pack()

# Create a frame for additional information
info_frame = tk.Frame(root)
info_frame.grid(row=1, columnspan=2, padx=5, pady=10)

# Create a Text widget for additional information
textbox = tk.Text(info_frame, height=5, width=80)
textbox.insert(tk.END, "This tool empowers you to optimize your stock portfolio allocation using Mean-Variance Optimization (MVO). Just put in your stocks and risk and watch your efficient frontier be created for you!!!")
textbox.pack()
textbox.config(state=tk.DISABLED)

# Create a frame for efficient frontier configuration
config_frame = tk.Frame(root)
config_frame.grid(row=2, columnspan=2, padx=5, pady=10)

# Create a label for instructions
label = tk.Label(config_frame, text="Efficient Frontier Configuration", font=('Arial', 20))
label.grid(row=0, columnspan=2)

# Create labels and entry fields using grid layout

start_year_label = tk.Label(config_frame, text="Start Year:", anchor=tk.W)
start_year_label.grid(row=1, column=0, padx=5, pady=5)

years = [str(year) for year in range(2000, 2025)]
var_start = tk.StringVar(root)
var_start.set("")
drop_start = OptionMenu(config_frame, var_start, *years)
drop_start.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

end_year_label = tk.Label(config_frame, text="End Year:", anchor=tk.W)
end_year_label.grid(row=2, column=0, padx=5, pady=5)

var_end = tk.StringVar(root)
var_end.set("Please Select an End Year")
drop_End = OptionMenu(config_frame, var_end, *years)
drop_End.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Create the initial stock entry widgets
symbol_label = tk.Label(config_frame, text="Enter stock symbol:", anchor=tk.W)
symbol_label.grid(row=3, column=0, padx=5, pady=5)

symbol_entry = tk.Entry(config_frame)
symbol_entry.grid(row=3, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="+ Add Stock Entry", command=add_stock_entry)
add_button.grid(row=4, column=0, padx=5, pady=5)

# List to keep track of stock entries
stock_entries = [(symbol_entry, config_frame)]

sv_ttk.set_theme("dark")

root.mainloop()