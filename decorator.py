import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        result["execution_time"] = f"{end - start:.6f} сек"
        return result
    return wrapper