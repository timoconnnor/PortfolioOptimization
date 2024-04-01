import tkinter as tk
import dataProcessing


def search_stock():
    query = entry.get()
    processed_data = dataProcessing.fetch_closing_prices(query)
    
    # Clear any existing result label
    result_label.config(text="")

    # Display the processed data
    if processed_data is not None:
        result_label.config(text=processed_data)
    else:
        result_label.config(text="No data found for the entered stock symbol.")
    





root = tk.Tk()
root.geometry("800x500")
root.title("Portfolio Optimization")



# Create a label for instructions
label = tk.Label(root, text="Please Enter Stock Symbol")
label.pack()

# Create a text entry widget
entry = tk.Entry(root, width=40)
entry.pack()

# Create a search button
search_button = tk.Button(root, text="Search", command=search_stock, font=('Arial', 18))
search_button.pack(padx=10, pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=('Arial', 14))
result_label.pack()


root.mainloop()