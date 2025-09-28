from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")    
    print(f"Current date and time: {formatted_datetime}")    
    return current_date 
def calculate_future_date(start_date):
    while True:
        try:
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    
    time_delta = timedelta(days=days_to_add)
    
    future_date = start_date + time_delta
    
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {formatted_future_date}")


if __name__ == "__main__":
    
    start_date = display_current_datetime()
    
    
    calculate_future_date(start_date)