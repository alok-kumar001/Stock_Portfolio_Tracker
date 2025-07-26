import csv

# Hardcoded stock prices (in USD)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 135,
    "MSFT": 330
}

def stock_tracker():
    print("📈 Welcome to the Simple Stock Tracker!\n")
    print("Available stocks:", ', '.join(stock_prices.keys()))

    portfolio = {}
    total_investment = 0

    while True:
        stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
        if stock == "DONE":
            break
        if stock not in stock_prices:
            print("❗ Stock not found. Please choose from the available list.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock} shares: "))
        except ValueError:
            print("❗ Please enter a valid number.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    print("\n🧾 Investment Summary:")
    print("-" * 30)
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = qty * price
        total_investment += value
        print(f"{stock}: {qty} shares × ${price} = ${value}")

    print("-" * 30)
    print(f"💰 Total Investment: ${total_investment}")

    # Optional: Save to file
    save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
    if save == "yes":
        filename = "stock_summary.csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock", "Quantity", "Price", "Value"])
            for stock, qty in portfolio.items():
                price = stock_prices[stock]
                value = qty * price
                writer.writerow([stock, qty, price, value])
            writer.writerow(["Total", "", "", total_investment])
        print(f"📂 Summary saved to '{filename}'")

# Run the tracker
stock_tracker()
