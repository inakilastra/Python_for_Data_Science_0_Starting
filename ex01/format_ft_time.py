import time

# Get the current timestamp in seconds since the epoch (January 1, 1970)
current_time = time.time()

# Format the timestamp in scientific notation
scientific_notation = "{:.2e}".format(current_time)

# Format the timestamp as a human-readable date string (month, day, year)
human_readable_date = time.strftime("%b %d %Y", time.localtime())

# Print the formatted output
print(f"Seconds since January 1, 1970: {current_time:.2f} or {scientific_notation} in scientific notation")
print(human_readable_date)
