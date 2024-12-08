from datetime import datetime

    
now = datetime.now()

# Format the date to be more readable
# Wed Nov  4 05:10:30 2020
formatted_date = now.strftime("%a %b %d %I:%M:%S %Y")

# Return the current date and time
print(formatted_date)
print(now)