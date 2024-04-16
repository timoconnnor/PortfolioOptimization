import tkinter as tk
from tkinter.ttk import OptionMenu
import dataProcessing
from tkinter import ttk

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
    
    # Create the label and entry widgets
    symbol_label = tk.Label(config_frame, text="Enter stock symbol:", anchor=tk.W, font=(12))
    symbol_label.pack(fill="x", padx=5, pady=5)

    symbol_entry = tk.Entry(config_frame)
    symbol_entry.pack(fill="x", padx=5, pady=5)

    # Update the stock_entries list
    stock_entries.append((symbol_entry, config_frame))

# Everything below are edits to the GUI

root = tk.Tk()
root.geometry("600x700")
root.title("Portfolio Optimization")

# Create a frame for welcome message
welcome_frame = tk.Frame(root)
welcome_frame.pack(fill="x", padx=5, pady=10)

# Create a label for welcome message
welcome_label = tk.Label(welcome_frame, text="Welcome to my Portfolio Optimization for my Invesco Internship Project!", font=('Arial', 16))
welcome_label.pack()

# Create a frame for additional information
info_frame = tk.Frame(root)
info_frame.pack(fill="x", padx=5, pady=10)

# Create a Text widget for additional information
textbox = tk.Text(info_frame, height=10, width=80, font=('timesnewroman', 9))
textbox.insert(tk.END, "This tool empowers you to optimize your stock portfolio allocation using Mean-Variance Optimization (MVO). Just put in your S&P 500 stocks along with their risk and watch your efficient frontier be created for you! Follow these steps: \n\n 1. Select Start and End years for Portoflio Optimization period \n 2. Put in Stock tickers \n 3. Adjust Allocation for stocks")
textbox.pack()
textbox.config(state=tk.DISABLED)

# Create a frame for efficient frontier configuration
config_frame = tk.Frame(root)
config_frame.pack(fill="both", expand=True, padx=5, pady=10)

# Create a label for instructions
label = tk.Label(config_frame, text="Efficient Frontier Configuration", font=('Arial', 20))
label.pack()

# Create labels and entry fields using grid layout
start_year_frame = tk.Frame(config_frame)
start_year_frame.pack(fill="x")
start_year_label = tk.Label(start_year_frame, text="Start Year:", anchor=tk.W)
start_year_label.pack(side="left", padx=5, pady=5)

years = [str(year) for year in range(2000, 2025)]
var_start = tk.StringVar(root)
var_start.set("")
drop_start = OptionMenu(start_year_frame, var_start, *years)
drop_start.pack(side="left", padx=5, pady=5, fill="x", expand=True)

end_year_frame = tk.Frame(config_frame)
end_year_frame.pack(fill="x")
end_year_label = tk.Label(end_year_frame, text="End Year:", anchor=tk.W)
end_year_label.pack(side="left", padx=5, pady=5)

var_end = tk.StringVar(root)
var_end.set("Please Select an End Year")
drop_End = OptionMenu(end_year_frame, var_end, *years)
drop_End.pack(side="left", padx=5, pady=5, fill="x", expand=True)

# Create the initial stock entry widgets
symbol_label = tk.Label(config_frame, text="Enter stock symbol:", anchor=tk.W)
symbol_label.pack(fill="x", padx=5, pady=5)

symbol_entry = tk.Entry(config_frame)
symbol_entry.pack(fill="x", padx=5, pady=5)

# Create the initial stock entry widgets
result_label = tk.Label(config_frame, text="Stock Data:", anchor=tk.W)
result_label.pack(fill="x", padx=5, pady=5)

search_stock_button = tk.Button(root, text="Search Stock Entry Data", command=search_stock)
search_stock_button.pack(fill="x", padx=5, pady=5)

add_button = tk.Button(root, text="+ Add Stock Entry", command=add_stock_entry)
add_button.pack(fill="x", padx=5, pady=5)

# List to keep track of stock entries
stock_entries = [(symbol_entry, config_frame)]

# Create a frame for theme change button
theme_frame = tk.Frame(root)
theme_frame.pack(fill="x", padx=5, pady=10)

# Set the initial theme
root.tk.call("source", "azure.tcl")
root.tk.call("set_theme", "light")

def change_theme():
    # NOTE: The theme's real name is azure-<mode>
    if root.tk.call("ttk::style", "theme", "use") == "azure-dark":
        # Set light theme
        root.tk.call("set_theme", "light")
    else:
        # Set dark theme
        root.tk.call("set_theme", "dark")

# Remember, you have to use ttk widgets
button = ttk.Button(theme_frame, text="Change theme!", command=change_theme)
button.pack(fill="x")

root.mainloop()
