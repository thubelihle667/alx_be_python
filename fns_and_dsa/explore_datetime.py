from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()  # Get current date and time
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it
    print("Current date and time:", formatted)

def calculate_future_date(days):
    current_date = datetime.now()  # Get current date
    future_date = current_date + timedelta(days=days)  # Add days
    formatted = future_date.strftime("%Y-%m-%d")  # Format
    print("Future date after", days, "days will be:", formatted)

if __name__ == "__main__":
    display_current_datetime()
    
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Error: Please enter a valid integer.")
