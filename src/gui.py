import tkinter as tk
from tkinter import OptionMenu
from tkinter import messagebox
from calculation import calculate_graph

class MyGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x700")
        self.root.title("Portfolio Optimization")

        # Create a frame for welcome message
        self.welcome_frame = tk.Frame(self.root)
        self.welcome_frame.pack(fill="x", padx=5, pady=10)

        # Create a label for welcome message
        self.welcome_label = tk.Label(self.welcome_frame, text="Welcome to my Portfolio Optimization for my Invesco Internship Project!", font=('Arial', 16))
        self.welcome_label.pack()

        # Create a frame for additional information
        self.info_frame = tk.Frame(self.root)
        self.info_frame.pack(fill="x", padx=5, pady=10)

        # Create a Text widget for additional information
        self.textbox = tk.Text(self.info_frame, height=10, width=80, font=('timesnewroman', 9))
        self.textbox.insert(tk.END, "This tool empowers you to optimize your stock portfolio allocation using Mean-Variance Optimization (MVO). Just put in your S&P 500 stocks along with their risk and watch your efficient frontier be created for you! Follow these steps: \n\n 1. Select Start and End years for Portoflio Optimization period \n 2. Put in Stock tickers \n 3. Adjust Allocation for stocks")
        self.textbox.pack()
        self.textbox.config(state=tk.DISABLED)

        # Create a frame for efficient frontier configuration
        self.config_frame = tk.Frame(self.root)
        self.config_frame.pack(fill="both", expand=True, padx=5, pady=10)

        # Create a label for instructions
        self.label = tk.Label(self.config_frame, text="Efficient Frontier Configuration", font=('Arial', 20))
        self.label.pack()

        # Create labels and entry fields using grid layout
        self.start_year_frame = tk.Frame(self.config_frame)
        self.start_year_frame.pack(fill="x")
        self.start_year_label = tk.Label(self.start_year_frame, text="Start Year:", anchor=tk.W)
        self.start_year_label.pack(side="left", padx=5, pady=5)

        years = [str(year) for year in range(2000, 2025)]
        self.var_start = tk.StringVar(self.root)
        self.var_start.set("Please Select a Start Year")
        drop_start = OptionMenu(self.start_year_frame, self.var_start, *years)
        drop_start.pack(side="left", padx=5, pady=5, fill="x", expand=True)

        self.end_year_frame = tk.Frame(self.config_frame)
        self.end_year_frame.pack(fill="x")
        self.end_year_label = tk.Label(self.end_year_frame, text="End Year:", anchor=tk.W)
        self.end_year_label.pack(side="left", padx=5, pady=5)

        self.var_end = tk.StringVar(self.root)
        self.var_end.set("Please Select an End Year")
        drop_End = OptionMenu(self.end_year_frame, self.var_end, *years)
        drop_End.pack(side="left", padx=5, pady=5, fill="x", expand=True)

        # Create the initial stock entry widgets
        self.symbol_label = tk.Label(self.config_frame, text="Enter stock symbol:", anchor=tk.W)
        self.symbol_label.pack(fill="x", padx=5, pady=5)

        self.symbol_entry = tk.Entry(self.config_frame)
        self.symbol_entry.pack(fill="x", padx=5, pady=5)

        # Create the initial stock entry widgets
        self.result_label = tk.Label(self.config_frame, text="Efficient Frontier Plot:", anchor=tk.W)
        self.result_label.pack(fill="x", padx=5, pady=5)

        # Create a frame for theme change button
        self.theme_frame = tk.Frame(self.root)
        self.theme_frame.pack(fill="x", padx=5, pady=10)

        add_button = tk.Button(self.theme_frame, text="+ Add Stock Entry", command=self.add_stock_entry)
        add_button.pack(fill="x", padx=5, pady=5)

        search_stock_button = tk.Button(self.theme_frame, text="Click Here to Create Plot", command=self.calculate_and_show_plot)
        search_stock_button.pack(fill="x", padx=5, pady=5)

        # List to keep track of stock entries
        self.stock_entries = [(self.symbol_entry, self.config_frame)]

        # Set the initial theme
        self.root.tk.call("source", "azure.tcl")
        self.root.tk.call("set_theme", "light")

    def get_inputs(self):
        # retrieve start year
        start_year = self.var_start.get()
        if not start_year:
            messagebox.showerror("Error", "Please select a start year")
            return
        
        # retrieve selected end year
        end_year = self.var_end.get()
        if not end_year:
            messagebox.showerror("Error", "Please select an end year")
            return
        
        stock_symbols = []
        for entry_widget, _ in self.stock_entries:
            symbol = entry_widget.get()
            if not symbol:
                messagebox.showerror("Error", "Please enter a stock symbol")
                return
            stock_symbols.append(symbol)

    def calculate_and_show_plot(self):
        start_year, end_year, stock_symbols = self.get_inputs()
        calculate_graph(start_year, end_year, stock_symbols)
        
        

    def add_stock_entry(self):
        # Create the label and entry widgets
        symbol_label = tk.Label(self.config_frame, text="Enter stock symbol:", anchor=tk.W, font=(12))
        symbol_label.pack(fill="x", padx=5, pady=5)

        symbol_entry = tk.Entry(self.config_frame)
        symbol_entry.pack(fill="x", padx=5, pady=5)

        # Update the stock_entries list
        self.stock_entries.append((symbol_entry, self.config_frame))

