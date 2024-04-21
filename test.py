import datetime


print(" Hi, Its Ritik here!!!\n\n")
# Get current date and time
current_datetime = datetime.datetime.now()

# Format the datetime object as a string
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

# Display the current date and time
print("Current Date and Time:", formatted_datetime)
