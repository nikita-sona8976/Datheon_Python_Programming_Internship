import csv
import datetime
import os

# Optional: yfinance for real-time stock prices (fallback included if not installed)
try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False

PORTFOLIO_FILE = "portfolio.csv"
LOG_FILE = "portfolio_performance_log.csv"

def initialize_portfolio():
    """Create a sample portfolio file if it doesn't exist."""
    if not os.path.exists(PORTFOLIO_FILE):
        with open(PORTFOLIO_FILE, mode='w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Ticker", "Quantity", "Buy_Price"])
            # Sample default holdings
            writer.writerow(["AAPL", "10", "150.0"])
            writer.writerow(["GOOGL", "5", "120.0"])
            writer.writerow(["TSLA", "8", "200.0"])

def get_current_price(ticker):
    """Fetch live market price or use fallback simulation."""
    if YFINANCE_AVAILABLE:
        try:
            stock = yf.Ticker(ticker)
            todays_data = stock.history(period="1d")
            if not todays_data.empty:
                return float(todays_data['Close'].iloc[-1])
        except Exception:
            pass
    
    # Fallback simulated prices if offline or yfinance is missing
    fallback_prices = {"AAPL": 185.50, "GOOGL": 142.25, "TSLA": 210.00, "MSFT": 420.00}
    return fallback_prices.get(ticker.upper(), 100.0)

def calculate_portfolio_valuation():
    initialize_portfolio()
    
    total_investment = 0.0
    current_valuation = 0.0

    print("\n==================================================================")
    print("                 STOCK PORTFOLIO PERFORMANCE TRACKER              ")
    print("==================================================================")
    print(f"{'Ticker':<10} {'Quantity':<10} {'Buy Price':<12} {'Current Price':<14} {'Current Value':<14} {'Profit/Loss':<12}")
    print("-" * 72)

    with open(PORTFOLIO_FILE, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ticker = row['Ticker'].upper()
            qty = float(row['Quantity'])
            buy_price = float(row['Buy_Price'])
            
            curr_price = get_current_price(ticker)
            
            inv_value = qty * buy_price
            curr_value = qty * curr_price
            pnl = curr_value - inv_value
            
            total_investment += inv_value
            current_valuation += curr_value
            
            print(f"{ticker:<10} {qty:<10} ${buy_price:<11.2f} ${curr_price:<13.2f} ${curr_value:<13.2f} ${pnl:<11.2f}")

    total_pnl = current_valuation - total_investment
    print("-" * 72)
    print(f"Total Investment       : ${total_investment:.2f}")
    print(f"Current Valuation      : ${current_valuation:.2f}")
    print(f"Total Profit / Loss    : ${total_pnl:.2f}")
    print("=" * 72)

    # Persist performance logs to CSV
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exists = os.path.exists(LOG_FILE)
    
    with open(LOG_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Total_Investment", "Current_Valuation", "Total_Profit_Loss"])
        writer.writerow([timestamp, round(total_investment, 2), round(current_valuation, 2), round(total_pnl, 2)])

    print(f"\n✅ Performance log successfully saved to '{LOG_FILE}' at {timestamp}")

if __name__ == "__main__":
    calculate_portfolio_valuation()