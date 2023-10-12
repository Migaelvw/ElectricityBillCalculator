import tkinter as tk
from tkinter import ttk, filedialog
from ttkthemes import ThemedStyle
import calculator  # Import the module containing the ElectricityBillCalculator

# Create a class for the ElectricityBillApp
class ElectricityBillApp:
    def __init__(self, root):
        # Initialize the application with the root window
        self.root = root
        root.title("Electricity Bill Calculator")  # Set the window title
        self.style = ThemedStyle(root)
        self.style.set_theme("breeze")  # Set the theme for the GUI

        # Create an instance of the ElectricityBillCalculator class from the Calculator module
        self.calculator = calculator.ElectricityBillCalculator()

        # Create the GUI widgets
        self.create_widgets()

    # Create the graphical user interface (GUI) elements
    def create_widgets(self):
        # Create a button to browse for a CSV file and link it to the calculate_bill method
        self.browse_button = ttk.Button(
            self.root, text="Browse CSV File", command=self.calculate_bill)
        self.browse_button.grid(row=0, column=0, padx=10, pady=10)

        # Create a label with instructions for the user
        self.instructions_label = ttk.Label(
            self.root, text="Please select a CSV file to calculate the electricity bill.", font=("Arial", 12))
        self.instructions_label.grid(row=1, column=0, padx=10, pady=5)

        # Create a frame to display the electricity bill details
        self.result_frame = ttk.LabelFrame(
            self.root, text="Electricity Bill Details")
        self.result_frame.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

    # Method to calculate the electricity bill
    def calculate_bill(self):
        # Open a file dialog to select a CSV file and get the file path
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")]
        )
        if not file_path:  # If no file is selected, return without calculating
            return

        # Use the calculator instance to calculate the energy consumed and transactions
        energy_consumed, transactions = self.calculator.calculate(file_path)

        # Display the results
        self.display_results(energy_consumed, transactions)

    # Method to display the results in the GUI
    def display_results(self, energy_consumed, transactions):
        # Clear any existing widgets in the result_frame
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        # Create a label to display the total energy consumed
        total_consumed_label = ttk.Label(
            self.result_frame, text=f'Total energy consumed: {energy_consumed:.2f} kWh', font=("Arial", 12)
        )
        total_consumed_label.grid(row=0, column=0, padx=10, pady=5)

        # Create a label for the list of individual transactions
        transaction_text = ttk.Label(
            self.result_frame, text='Individual Transactions:', font=("Arial", 12)
        )
        transaction_text.grid(row=1, column=0, padx=10, pady=5)

        # Create labels for each transaction in the list
        for i, (range_start, range_end, consumed, cost) in enumerate(transactions):
            label_text = f'Range: {range_start} - {range_end} kWh, Consumed: {consumed:.2f} kWh, Cost: R {cost:.2f}'
            transaction_label = ttk.Label(
                self.result_frame, text=label_text, font=("Arial", 12)
            )
            transaction_label.grid(row=i + 2, column=0, padx=10, pady=5)

# Entry point for the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    # Create an instance of the ElectricityBillApp
    app = ElectricityBillApp(root)
    root.mainloop()  # Start the main event loop for the GUI
