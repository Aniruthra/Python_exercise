import time
"""
To find the time taken by functions using decorators
"""
def timer(func):
    def wrapper(*args, **kwargs):
        start=time.time()
        result=func(*args, **kwargs)
        end=time.time()
        duration=end-start
        print(f"The output for the function {func.__name__}is :{result}, duration to run the function is {duration}")
        return result
    return wrapper

'''here @timer is the decorator which means everytime when the square function is called,
it first run the timer function and then run the squares function which is passed as an argument to timer function'''
@timer
def squares(*numbers):
    result=[x*x for x in numbers]
    return result

ans=squares(1,2,3,4)
print(f"The answer is :{ans}")

@timer
def even(*nums):
    output=[i for i in nums if i%2==0]
    return output

answer=even(1,2,3,4,5)
print(f"the even numbers are : {answer}")