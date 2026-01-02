def my_decorator (func):
    
    def wrapper():
        print("Before function runs")
        # func()
        print("After function runs")
    
    return wrapper 

@my_decorator
def greet():
    print("Hi How are you doing today ?")
    
greet()