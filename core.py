from datetime import datetime

def log(message: str, *, time: bool = True):
    time = datetime.now().strftime("[%H:%M:%S]")
    print(f"{time} {message}")