import datetime


def now():
    now = datetime.now()
    formatted_date = now.strftime("%D%M%Y_%H%M%S")  # Format: DDMMYYYY_HHMMSS

    return formatted_date
