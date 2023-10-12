# Import necessary libraries
import sys
import pandas as pd

# Create a class for electricity bill calculation
class ElectricityBillCalculator:
    def __init__(self):
        # Define tariff rates for different energy consumption ranges
        self.tariff_rates = {
            (0, 100): 241.37,         # Tariff rate for the first 100 kWh
            (101, 400): 282.47,       # Tariff rate for the next 300 kWh
            (401, 650): 307.75,       # Tariff rate for the next 250 kWh
            (651, float('inf')): 331.76,  # Tariff rate for consumption above 650 kWh
        }
    
    def calculate(self, file_path):
        # Read data from a CSV file using Pandas
        try:
            df = pd.read_csv(file_path)
            meter_readings = df['forwardActiveEnergy Value']        
        except:
            print("Error: Invalid CSV file.")
            sys.exit(1)

        initial_reading = meter_readings.iloc[0]
        final_reading = meter_readings.iloc[-1]
        
        # Calculate the energy consumed in kWh
        energy_consumed = ((final_reading - initial_reading) / 2) / 1000  # Convert W to kWh as readings are in W0.5h
        transactions = []

        remaining_consumption = energy_consumed
        
        # Calculate transactions based on energy consumption ranges and tariff rates
        for (range_start, range_end), rate in self.tariff_rates.items():
            if remaining_consumption <= 0:
                break
            if remaining_consumption <= (range_end - range_start):
                cost = remaining_consumption * rate / 100  # Convert to R
                transactions.append((range_start, range_end, remaining_consumption, cost))
                break
            else:
                cost = (range_end - range_start) * rate / 100  # Convert to R
                transactions.append((range_start, range_end, range_end - range_start, cost))
                remaining_consumption -= (range_end - range_start)
        
        return energy_consumed, transactions

# Check if the script is run as the main program
if __name__ == "__main__":
    # Check if the correct number of command-line arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python calculator.py <csv_file>")
        sys.exit(1)

    # Get the CSV file path from the command-line arguments
    csv_file = sys.argv[1]

    # Create an instance of the ElectricityBillCalculator class
    calculator = ElectricityBillCalculator()

    # Calculate the energy consumption and transactions
    energy_consumed, transactions = calculator.calculate(csv_file)

    # Print the results
    print(f'Total energy consumed: {energy_consumed:.2f} kWh')
    print('Individual Transactions:')
    for range_start, range_end, consumed, cost in transactions:
        print(f'Range: {range_start} - {range_end} kWh, Consumed: {consumed:.2f} kWh, Cost: R {cost:.2f}')
