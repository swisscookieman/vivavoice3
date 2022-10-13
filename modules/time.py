from datetime import datetime



def time_function():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time
