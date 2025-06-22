import time
def divide(a, b):
    return a / b

def run(a, b, retry_time = 1):
    result = None
    try:  # dealing with user input, opening files, connecting the web ...
        print(10/4)
        print(100/1.3)
        print(432/-3)
        print(a/b)
        result =  divide(a,b)
        # open("this-doesn't-exist")
        # int("This is not a number")
    except ZeroDivisionError:  # more granular/specific
        print("You tried to divide by zero!")
        time.sleep(retry_time)  # exponential backoff
        new_retry_time = 2 * retry_time
        print(new_retry_time)
        if new_retry_time > 30:
            raise ZeroDivisionError("We tried - it's really not working!")
        run(a, 0, new_retry_time)
    except FileNotFoundError as exp:
        print("Whoops! We don't have that file!")
        # log_to_oncall(exp)
    except Exception as exp:  # least specific - more general
        print(exp)
    else:
        print("I will only run if nothing went wrong and the try block completed")
    finally:
        # tidy up - close the file, close the connection
        print("Will always run after the try/except blocks")
    return result

run(10,1)