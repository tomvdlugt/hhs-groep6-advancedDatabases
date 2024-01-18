import datetime

def now():
    current_time = datetime.datetime.now()  # Get the current date and time
    formatted_date = current_time.strftime("%d%m%Y_%H%M%S")  # Format: DDMMYYYY_HHMMSS

    return formatted_date
