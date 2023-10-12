# Electricity Bill Calculator

**Author: Migael van Wyk**

The Electricity Bill Calculator is a Python application that calculates the cost of electricity consumption based on user-provided meter readings. It provides a user-friendly graphical user interface (GUI) for selecting a CSV file containing meter readings and displays the total energy consumed and the cost in different consumption ranges.

## Features

- Select a CSV file with meter readings to calculate the electricity bill.
- Calculate the total energy consumed in kilowatt-hours (kWh) and display it.
- Calculate the cost of electricity consumption in different consumption ranges based on predefined tariff rates.
- Display individual transactions showing the range, consumed energy, and cost.

## Prerequisites

Before running the Electricity Bill Calculator, make sure you have the following prerequisites installed:

- Python 3
- Python libraries mentioned in the `requirements.txt` file
- Tkinter library for GUI (install it using `sudo apt-get install python3-tk`)

## Installation

1. Clone or download the project to your local machine.

2. Navigate to the project directory.

3. Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

# Usage

To use the Electricity Bill Calculator, follow these steps:

1. Clone or download the project to your local machine.

2. Navigate to the project directory.

3. Run the app:

   **Option 1: Using the Provided Bash Script**

    For Unix shell, run the following command in your terminal:

   ```bash
    bash run.sh
   ```

   **Option 2: Running the calculator on it's own**
   ```
   python3 calculator.py <csv file>
   ```

   Replace csv file with the path to your CSV file containing meter readings.
## CSV File Format

The application expects a CSV file with at least one column named "forwardActiveEnergy Value" containing meter readings in Watt units. The readings are typically taken at regular intervals, such as every half-hour.

## Customization

You can customize the tariff rates by modifying the `tariff_rates` dictionary in the `calculator.py` script. Update the consumption ranges and rates as needed.

```python
self.tariff_rates = {
    (0, 100): 241.37,         # Tariff rate for the first 100 kWh
    (101, 400): 282.47,       # Tariff rate for the next 300 kWh
    (401, 650): 307.75,       # Tariff rate for the next 250 kWh
    (651, float('inf')): 331.76,  # Tariff rate for consumption above 650 kWh
}
```
## How to Use

1. Launch the Electricity Bill Calculator using the `run.sh` script.

2. Click the "Browse CSV File" button to select a CSV file containing meter readings.

3. The application will calculate the total energy consumed and display it, along with individual transactions.

4. If no file is selected, the application will do nothing. You can close the file dialog.

## Acknowledgments

- This project uses the [Pandas](https://pandas.pydata.org/) library for reading CSV files and data manipulation.
- The GUI theme is provided by the [ttkthemes](https://github.com/RedFantom/ttkthemes) library.

Enjoy calculating your electricity bill with this handy tool! If you encounter any issues or have suggestions for improvements, please feel free to [contribute](CONTRIBUTING.md) or report them in the [issues](https://github.com/your/repository/issues) section.
