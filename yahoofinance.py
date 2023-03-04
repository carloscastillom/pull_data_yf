from yahooquery import Ticker
import csv


def get_financials(symbol):
    ticker = Ticker(symbol)

    financials = ticker.financial_data
    if not financials:
        raise Exception("No financial data available for the symbol")

    # Write financial data to a CSV file
    filename = f"{symbol}_financials.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Metric", "Value"])
        for key, value in financials.items():
            writer.writerow([key, value])
    return filename

