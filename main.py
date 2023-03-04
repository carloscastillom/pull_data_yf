import tkinter as tk
from yahoofinance import get_financials


class FinancialsApp:
    def __init__(self, master):
        self.master = master
        master.title("Financial Statements Downloader")

        self.label = tk.Label(master, text="Enter stock symbol:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Download", command=self.download)
        self.button.pack()

        self.status_label = tk.Label(master, text="")
        self.status_label.pack()

    def download(self):
        symbol = self.entry.get().strip().upper()
        if not symbol:
            self.status_label.configure(text="Please enter a stock symbol")
            return

        try:
            get_financials(symbol)
            self.status_label.configure(text="Financial statements downloaded successfully!")
        except Exception as e:
            self.status_label.configure(text=f"Error downloading financial statements: {str(e)}")


if __name__ == '__main__':
    root = tk.Tk()
    app = FinancialsApp(root)
    root.mainloop()
