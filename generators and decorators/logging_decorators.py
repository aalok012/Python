from functools  import wraps

def log_activity(func): 
    
    @wraps(func)
    def wrapper(*args, **kwrags):
        print(f"Calling: {func.__name__}")
        result= func(*args, **kwrags)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def balanzo(type):
    print(f"Tracking your {type} expenses")

balanzo("daily")